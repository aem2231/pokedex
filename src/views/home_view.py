import customtkinter as ctk
import keyboard
from utils.helper import Helper
import random

class HomeView(ctk.CTkFrame):
    def __init__(self, master) -> None:
        self.user = Helper.get_username()
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

        search_box = ctk.CTkEntry(self, width=300, placeholder_text="Search")
        search_box.grid(row=0, column=0, columnspan=3, padx=10, pady=10, sticky="n")

        search_button = ctk.CTkButton(self, text="Search", command=self.search)
        search_button.grid(row=1, column=0, columnspan=3, padx=10, pady=10, sticky="n")

        message = ctk.CTkLabel(self, text=f"{self.get_greeting()} {self.user}!", font=('Arial', 30))
        message.grid(row=2, column=0, columnspan=3, padx=10, pady=10, sticky="n")

        padding_x = 10
        padding_y = 10

        # Create and place the buttons dynamically
        buttons = []
        for i in range(6):
            button = ctk.CTkButton(self, text="", height=200, width=200)
            row = 3 + i // 3
            column = i % 3
            button.grid(row=row, column=column, padx=padding_x, pady=padding_y)
            buttons.append(button)

    def search(self):
        print("search button clicked")

    def get_greeting(self) -> str:
        greetings = {
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
