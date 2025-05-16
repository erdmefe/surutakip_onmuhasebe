import customtkinter as ctk

class MainView(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        self.pack_propagate(False)
        self.current_page = None

    def load_page(self, title):
        if self.current_page:
            self.current_page.destroy()
        self.current_page = ctk.CTkFrame(self)
        self.current_page.pack(expand=True, fill="both")
        label = ctk.CTkLabel(self.current_page, text=title, font=ctk.CTkFont(size=20))
        label.pack(pady=20)
