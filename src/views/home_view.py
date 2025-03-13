from os import confstr_names
import customtkinter as ctk
from utils.helper import Helper
from models.home_model import HomeModel
import random
from typing import Callable

class HomeView(ctk.CTkFrame):
    def __init__(self, master) -> None:
        self.user: str = Helper.get_username()
        self.HomeModel = HomeModel()
        super().__init__(master)
        self.master = master
        self.create_ui()
        self.pack(expand=True, fill="both")

    def create_ui(self) -> None:
        # Configure the grid to center the widgets
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure(2, weight=1)
        self.grid_rowconfigure(0, weight=0)
        self.grid_rowconfigure(1, weight=0)
        self.grid_rowconfigure(2, weight=0)
        self.grid_rowconfigure(3, weight=0)
        self.grid_rowconfigure(4, weight=0)
        self.grid_rowconfigure(5, weight=1)  # This row will expand to fill the remaining space

        self.search_box: ctk.CTkEntry = ctk.CTkEntry(self, width=300, placeholder_text="Search")
        self.search_box.grid(row=0, column=0, columnspan=3, padx=10, pady=10, sticky="n")

        search_button: ctk.CTkButton = ctk.CTkButton(self, text="Search", command=self.start_search())
        search_button.grid(row=0, column=1, columnspan=3, padx=10, pady=10, sticky="n")

        message = ctk.CTkLabel(self, text=f"{self.get_greeting()} {self.user}!", font=('Arial', 30))
        message.grid(row=2, column=0, columnspan=3, padx=10, pady=10, sticky="n")

        padding_x: int = 10
        padding_y: int = 10
        button_names: list[str] = ["poke1", "poke2", "poke3", "poke4", "poke5", "poke6"]
        positions: list[tuple[int, int]] = [(3, 0), (3, 1), (3, 2), (4, 0), (4, 1), (4, 2)]

        for name, (row, col) in zip(button_names, positions):
            button: ctk.CTkButton = ctk.CTkButton(self, text="", height=200, width=200, command=self.create_command(name))
            button.name = name # Assign a custom attribute 'name' to the buttons
            button.grid(row=row, column=col, padx=padding_x, pady=padding_y)

    def create_command(self, button_name: str) -> Callable[[], None]:
        return lambda: self.HomeModel.poke_on_click_handler(button_name)

    def start_search(self) -> Callable[[], None]:
        return lambda: self.HomeModel.search(self.search_box.get())

    def get_greeting(self) -> str:
        greetings: dict[int, str] = {
            1: "Hi",
            2: "How's it going",
            3: "Hello",
            4: "Hey",
            5: "What's up ",
            6: "Howdy",
            7: "Greetings"
            }

        greeting: str = greetings[random.randint(1, 7)]
        return greeting
