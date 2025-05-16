import customtkinter as ctk
from ui.sidebar import Sidebar
from ui.main_view import MainView

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Livestock Management System")
        self.geometry("1000x600")
        ctk.set_appearance_mode("light")
        ctk.set_default_color_theme("blue")

        # Layout
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        # Main View
        self.main_view = MainView(self)
        self.main_view.grid(row=0, column=1, sticky="nsew", padx=10, pady=10)

        # Page callback dictionary
        callbacks = {
            "Dashboard": lambda: self.main_view.load_page("Dashboard"),
            "Add Animal": lambda: self.main_view.load_page("Add Animal"),
            "Animal Info": lambda: self.main_view.load_page("Animal Info"),
            "Health Data" : lambda: self.main_view.load_page("Health Data"),
            "Pregnancy Status": lambda: self.main_view.load_page("Pregnancy Status"),
            "Milking Data": lambda: self.main_view.load_page("Milking Data"),
            "Feed Ration": lambda: self.main_view.load_page("Feed Ration"),
            "Feed Stock": lambda: self.main_view.load_page("Feed Stock"),
            "Quarantine": lambda: self.main_view.load_page("Quarantine"),
            "Historical Data": lambda: self.main_view.load_page("Historical Data"),
            "Accounting": lambda: self.main_view.load_page("Accounting"),
            "Settings": lambda: self.main_view.load_page("Settings"),
        }

        # Sidebar
        self.sidebar = Sidebar(self, callbacks)
        self.sidebar.grid(row=0, column=0, sticky="ns")

        # Start with Dashboard
        self.main_view.load_page("Dashboard")


if __name__ == "__main__":
    app = App()
    app.mainloop()
