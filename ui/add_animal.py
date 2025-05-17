import customtkinter as ctk
from tkinter import filedialog
from PIL import Image
import os
from data.database import insert_animal

class AddAnimalPage(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)
        self.inputs = {}
        self.image_path = ""

        self.grid_columnconfigure(0, weight=1)
        form_frame = ctk.CTkFrame(self)
        form_frame.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")
        form_frame.grid_columnconfigure(0, weight=1)

        fields = [
            ("Tag No*", "tag_no"),
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
            label = ctk.CTkLabel(form_frame, text=label_text)
            entry = ctk.CTkEntry(form_frame)
            label.grid(row=i * 2, column=0, sticky="w")
            entry.grid(row=i * 2 + 1, column=0, sticky="ew", pady=(0, 10))
            self.inputs[key] = entry

        self.image_btn = ctk.CTkButton(form_frame, text="Upload Image", command=self.upload_image)
        self.image_btn.grid(row=len(fields) * 2, column=0, pady=(10, 0))

        submit_btn = ctk.CTkButton(form_frame, text="Submit", command=self.submit)
        submit_btn.grid(row=len(fields) * 2 + 1, column=0, pady=(10, 0))

    def upload_image(self):
        path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg *.jpeg *.png")])
        if path:
            self.image_path = path

    def submit(self):
        data = {key: entry.get().strip() for key, entry in self.inputs.items()}
        if not data["tag_no"]:
            print("Tag No is required.")
            return
        data["image"] = self.image_path
        insert_animal(data)
        print("Animal saved successfully.")
        for entry in self.inputs.values():
            entry.delete(0, "end")
        self.image_path = ""
