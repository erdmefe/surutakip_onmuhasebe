import customtkinter as ctk
from tkinter import ttk
from tkinter import Toplevel
from tkinter import filedialog
from PIL import Image, ImageTk
from data.database import fetch_all_animals
import os

class AnimalInfoPage(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)
        self.grid_columnconfigure(0, weight=3)
        self.grid_columnconfigure(1, weight=2)
        self.grid_rowconfigure(1, weight=1)
        self.animals = [dict(zip((
        "tag_no", "institution_no", "name", "breed", "gender", "birth_date",
        "pregnancy_count", "status", "vaccination_date", "last_birth_date", "image"
        ), row)) for row in fetch_all_animals()]

        search_frame = ctk.CTkFrame(self)
        search_frame.grid(row=0, column=0, columnspan=2, sticky="ew", padx=10, pady=10)
        search_frame.grid_columnconfigure(0, weight=1)

        self.search_entry = ctk.CTkEntry(search_frame, placeholder_text="Search by Tag No...")
        self.search_entry.grid(row=0, column=0, sticky="ew", padx=(0, 10))
        self.search_entry.bind("<KeyRelease>", self.perform_search)

        self.tree = ttk.Treeview(self, columns=("tag_no", "institution_no", "name", "breed", "gender",
                                                "birth_date", "pregnancy_count", "status",
                                                "vaccination_date", "last_birth_date"), show="headings")

        headings = ["Tag No", "Institution No", "Name", "Breed", "Gender", "Birth Date",
                    "Pregnancy Count", "Status", "Vaccination Date", "Last Birth Date"]

        for col, title in zip(self.tree["columns"], headings):
            self.tree.heading(col, text=title)
            self.tree.column(col, width=120, minwidth=100, stretch=True)

        self.tree.grid(row=1, column=0, sticky="nsew", padx=10, pady=10)
        self.tree.bind("<Double-1>", self.edit_animal)
        self.tree.bind("<<TreeviewSelect>>", self.show_image)

        # Scrollbars
        vsb = ttk.Scrollbar(self, orient="vertical", command=self.tree.yview)
        hsb = ttk.Scrollbar(self, orient="horizontal", command=self.tree.xview)
        self.tree.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)
        vsb.grid(row=1, column=0, sticky="nse", padx=(0, 10))
        hsb.grid(row=2, column=0, sticky="ew", padx=10)

        self.image_frame = ctk.CTkFrame(self)
        self.image_frame.grid(row=1, column=1, sticky="nsew", padx=10, pady=10)
        self.image_frame.grid_rowconfigure(0, weight=1)
        self.image_frame.grid_columnconfigure(0, weight=1)

        self.image_label = ctk.CTkLabel(self.image_frame, text="Image Preview")
        self.image_label.grid(row=0, column=0, sticky="nsew")

    def perform_search(self, event):
        query = self.search_entry.get().lower()
        self.tree.delete(*self.tree.get_children())

        for animal in self.animals:
            if any(query in str(value).lower() for value in animal.values()):
                self.tree.insert("", "end", values=tuple(animal.values())[:-1])  # skip image path

    def show_image(self, event):
        selected = self.tree.selection()
        if not selected:
            return
        values = self.tree.item(selected[0], "values")
        tag_no = values[0]
        animal = next((a for a in self.animals if a["tag_no"] == tag_no), None)
        if animal:
            try:
                img = Image.open(animal["image"])
                img = img.resize((250, 250), Image.ANTIALIAS)
                photo = ImageTk.PhotoImage(img)
                self.image_label.configure(image=photo, text="")
                self.image_label.image = photo
            except:
                self.image_label.configure(text="No Image Found", image=None)

    def edit_animal(self, event):
        selected = self.tree.selection()
        if not selected:
            return
        values = self.tree.item(selected[0], "values")
        tag_no = values[0]
        animal = next((a for a in self.animals if a["tag_no"] == tag_no), None)
        if animal:
            EditAnimalPopup(self, animal, self.refresh_table)

    def refresh_table(self):
        for item in self.tree.get_children():
            self.tree.delete(item)
        for animal in self.animals:
            self.tree.insert("", "end", values=tuple(animal.values()))

class EditAnimalPopup(Toplevel):
    def __init__(self, parent, animal_data, refresh_callback):
        super().__init__()
        self.title("Edit Animal")
        self.geometry("500x600")
        self.animal_data = animal_data
        self.refresh_callback = refresh_callback
        self.entries = {}

        container = ctk.CTkFrame(self)
        container.pack(expand=True, fill="both", padx=20, pady=20)
        container.grid_columnconfigure(0, weight=1)

        fields = [
            ("Institution No", "institution_no"),
            ("Name", "name"),
            ("Breed", "breed"),
            ("Gender", "gender"),
            ("Birth Date", "birth_date"),
            ("Pregnancy Count", "pregnancy_count"),
            ("Status", "status"),
            ("Vaccination Date", "vaccination_date"),
            ("Last Birth Date", "last_birth_date")
        ]

        for i, (label_text, key) in enumerate(fields):
            label = ctk.CTkLabel(container, text=label_text)
            entry = ctk.CTkEntry(container)
            entry.insert(0, animal_data.get(key, ""))
            label.grid(row=i * 2, column=0, sticky="w", pady=(5, 0))
            entry.grid(row=i * 2 + 1, column=0, sticky="ew", pady=(0, 10))
            self.entries[key] = entry

        save_btn = ctk.CTkButton(container, text="Save", command=self.save)
        save_btn.grid(row=len(fields) * 2 + 1, column=0, pady=20, sticky="ew")

    def save(self):
        for key, entry in self.entries.items():
            self.animal_data[key] = entry.get()
        self.refresh_callback()
        self.destroy()
