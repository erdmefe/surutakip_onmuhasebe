import customtkinter as ctk

class Sidebar(ctk.CTkFrame):
    def __init__(self, master, app_callback_dict):
        super().__init__(master, width=180)
        self.grid_propagate(False)
        self.app_callback_dict = app_callback_dict
        self.livestock_open = False
        self.grid_columnconfigure(0, weight=1)

        for i in range(20):
            self.grid_rowconfigure(i, weight=0)

        row = 0
        self.dashboard_btn = ctk.CTkButton(self, text="Dashboard", command=self.app_callback_dict["Dashboard"])
        self.dashboard_btn.grid(row=row, column=0, pady=(10, 0), padx=10, sticky="ew")
        row += 1

        self.livestock_toggle_btn = ctk.CTkButton(self, text="Livestock Management ▸", command=self.toggle_livestock_menu)
        self.livestock_toggle_btn.grid(row=row, column=0, pady=(10, 0), padx=10, sticky="ew")
        row += 1

        self.livestock_frame = ctk.CTkFrame(self, fg_color="transparent")
        self.livestock_frame.grid(row=row, column=0, padx=20, sticky="ew")
        self.livestock_frame.grid_remove()
        row += 1

        self.livestock_tabs = [
            ("Add Animal", self.app_callback_dict["Add Animal"]),
            ("Animal Info", self.app_callback_dict["Animal Info"]),
            ("Health Data", self.app_callback_dict["Health Data"]),
            ("Pregnancy Status", self.app_callback_dict["Pregnancy Status"]),
            ("Milking Data", self.app_callback_dict["Milking Data"]),
            ("Feed Ration", self.app_callback_dict["Feed Ration"]),
            ("Feed Stock", self.app_callback_dict["Feed Stock"]),
            ("Quarantine", self.app_callback_dict["Quarantine"]),
            ("Historical Data", self.app_callback_dict["Historical Data"]),
        ]

        self.livestock_buttons = []
        for i, (name, cmd) in enumerate(self.livestock_tabs):
            btn = ctk.CTkButton(
                self.livestock_frame,
                text=name,
                command=cmd,
                height=30,
                fg_color="#d9d9d9",
                text_color="black",
                anchor="w",
                corner_radius=5
            )
            btn.grid(row=i, column=0, pady=2, sticky="ew")
            self.livestock_buttons.append(btn)

        self.accounting_btn = ctk.CTkButton(self, text="Accounting", command=self.app_callback_dict["Accounting"])
        self.accounting_btn.grid(row=row, column=0, pady=(10, 5), padx=10, sticky="ew")
        row += 1

        self.settings_btn = ctk.CTkButton(self, text="Settings", command=self.app_callback_dict["Settings"])
        self.settings_btn.grid(row=row, column=0, pady=(5, 10), padx=10, sticky="ew")
        row += 1

        self.appearance_mode = ctk.CTkSwitch(self, text="Dark Mode", command=self.toggle_mode)
        self.appearance_mode.grid(row=row, column=0, pady=(5, 10), padx=10, sticky="ew")
        row += 1

    def toggle_livestock_menu(self):
        self.livestock_open = not self.livestock_open
        if self.livestock_open:
            self.livestock_toggle_btn.configure(text="Livestock Management ▾")
            self.livestock_frame.grid()
        else:
            self.livestock_toggle_btn.configure(text="Livestock Management ▸")
            self.livestock_frame.grid_remove()

    def toggle_mode(self):
        mode = "dark" if self.appearance_mode.get() else "light"
        ctk.set_appearance_mode(mode)
