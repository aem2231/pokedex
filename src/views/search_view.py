from utils.helper import Helper
import customtkinter as ctk
from typing import Callable
from models.search_model import SearchModel

class SearchView(ctk.CTkFrame):
    def __init__(self, master) -> None:
        super().__init__(master)
        self.create_ui()
        self.pack(expand=True, fill="both")
        self.SearchModel = SearchModel(self)


    def create_ui(self) -> None:
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure(2, weight=1)
        self.grid_columnconfigure(3, weight=1)
        self.grid_columnconfigure(4, weight=1)
        self.grid_rowconfigure(0, weight=0)
        self.grid_rowconfigure(1, weight=0)
        self.grid_rowconfigure(2, weight=0)
        self.grid_rowconfigure(3, weight=0)
        self.grid_rowconfigure(4, weight=0)

        padding_x: int = 10
        padding_y: int = 10

        button_names: list[str] = ["1", "2", "3", "4", "5"]
        positions: list[tuple[int, int]] = [(1, 1), (1, 2), (1, 3), (1, 4), (1, 5)]


        for name, (row, col) in zip(button_names, positions):
            button: ctk.CTkButton = ctk.CTkButton(self, text="", height=200, width=200, command=self.create_command(name))
            button.name = name # Assign a custom attribute 'name' to the buttons
            button.grid(row=row, column=col, padx=padding_x, pady=padding_y)


    def create_command(self, button_name: str) -> Callable[[], None]:
        return lambda: print(f"Button {button_name} clicked")
