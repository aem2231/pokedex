import customtkinter as ctk

class HomeView(ctk.CTkFrame):
    def __init__(self, master) -> None:
        super().__init__(master)
        self.master = master
        self.create_ui()
        self.pack(expand=True, fill="both")

    def create_ui(self) -> None:
        pass
