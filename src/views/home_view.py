from enum import IntEnum
import customtkinter as ctk
from utils.helper import Helper
from models.home_model import HomeModel
import random
import pandas as pd
from typing import Callable
from api.pokemon import Pokemon
from PIL import Image
from pathlib import Path
from utils.helper import Helper

class HomeView(ctk.CTkFrame):
    def __init__(self, master) -> None:
        super().__init__(master)
        self.user: str = Helper.get_username()
        self.Pokemon = Pokemon()
        self.HomeModel = HomeModel(self)
        self.Helper = Helper()
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
        self.grid_rowconfigure(5, weight=1)

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

        pokemon: list[str] = self.HomeModel.get_pokemon()
        pokemon_sprites: list = []

        r: int = 0
        for p in pokemon:
            pokemon_sprites.append(self.Pokemon.get_pokemon_image(int(p), r))

        pokemon_names: list[str] = self.Helper.get_pokemon_names(pokemon)

        i: int = 0
        for name, (row, col) in zip(button_names, positions):
            try:
                pokemon_id = int(pokemon[i])
                image_path = Path.cwd() / "data" / "images" / f"poke{pokemon_id}.png"

                if not image_path.exists():
                    self.Pokemon.get_pokemon_image(pokemon_id, pokemon_id)

                pokemon_image = ctk.CTkImage(
                    dark_image=Image.open(image_path),
                    light_image=Image.open(image_path),
                    size=(150, 150)
                )

                button: ctk.CTkButton = ctk.CTkButton(
                    self,
                    text=f"{pokemon_names[i]}",
                    image=pokemon_image,
                    height=200,
                    width=200,
                    compound="top",
                    command=self.create_command(name)
                )
                button.name = name
                button.grid(row=row, column=col, padx=padding_x, pady=padding_y)

                i += 1

            except Exception as e:
                print(f"Error loading Pokemon image: {e}")
                button: ctk.CTkButton = ctk.CTkButton(
                    self,
                    text="Pokemon",
                    height=200,
                    width=200,
                    command=self.create_command(name)
                )
                button.name = name
                button.grid(row=row, column=col, padx=padding_x, pady=padding_y)

    def create_command(self, button_name: str) -> Callable[[], None]:
        return lambda: self.HomeModel.poke_on_click_handler(button_name)


    def start_search(self) -> Callable[[], None]:
        return lambda: self.switch_to_search_view()

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

    def switch_to_search_view(self) -> None:
        query = self.search_box.get()
        if query != "":  # only search if there's a query
            print("search clicked")
            result = self.HomeModel.search_pokemon(query)
            print(result)
            self.Helper.save_result_names(result)
            from views.search_view import SearchView
            self.master.show_view(SearchView)

# i hate this
