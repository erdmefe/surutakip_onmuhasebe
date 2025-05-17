import customtkinter as ctk

from ui.add_animal import AddAnimalPage
from ui.animal_info import AnimalInfoPage

class MainView(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        self.pack_propagate(False)
        self.current_page = None

    def load_page(self, title):
        if self.current_page:
            self.current_page.destroy()

        if title == "Add Animal":
            self.current_page = AddAnimalPage(self)
        elif title == "Animal Info":
            self.current_page = AnimalInfoPage(self)
        else:
            self.current_page = ctk.CTkFrame(self)
            label = ctk.CTkLabel(self.current_page, text=title, font=ctk.CTkFont(size=20))
            label.pack(pady=20)

        self.current_page.pack(expand=True, fill="both")
