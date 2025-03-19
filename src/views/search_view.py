from utils.helper import Helper
import customtkinter as ctk
from typing import Callable
from models.search_model import SearchModel
from models.home_model import HomeModel
from PIL import Image
from utils.helper import Helper

class SearchView(ctk.CTkFrame):
    def __init__(self, master) -> None:
        super().__init__(master)
        self.master = master
        self.SearchModel = SearchModel(self)
        self.create_ui()
        self.Helper = Helper()
        self.grid(row=0, column=0, sticky="nsew")
        self.name = self.Helper.get_username()

    def create_ui(self) -> None:
        # Configure the grid for consistent layout
        for col in range(3):  # Adjust the number of columns as needed
            self.grid_columnconfigure(col, weight=1)
        for row in range(7):  # Adjust the number of rows as needed
            self.grid_rowconfigure(row, weight=1)

        # Back button at the top-left corner
        back_button: ctk.CTkButton = ctk.CTkButton(
            self,
            text="Back",
            command=self.go_back,
            width=100
        )
        back_button.grid(row=0, column=0, padx=10, pady=10, sticky="nw")

        # Padding and button configuration
        padding_x: int = 10
        padding_y: int = 10
        button_names: list[str] = ["button1", "button2", "button3", "button4", "button5", "button6", "button7", "button8", "button9", "button10"]
        positions: list[tuple[int, int]] = [
            (1, 0), (1, 1), (1, 2),  # First row of buttons
            (2, 0), (2, 1), (2, 2),  # Second row of buttons
            (3, 0), (3, 1), (3, 2),  # Third row of buttons
            (4, 1)                   # Centered button in the last row
        ]


        i: int = 0
        result_names: list[str] = Helper.load_result_names()
        print(result_names)

        # Create buttons and place them in the grid
        for name, (row, col) in zip(button_names, positions):
            image_path = self.SearchModel.get_image(result_names[i])

            if image_path and image_path.exists():
                pokemon_image = ctk.CTkImage(
                    dark_image=Image.open(image_path),
                    light_image=Image.open(image_path),
                    size=(150, 150)
                )
            else:
                image_path = Helper.get_placeholder_image()
                if image_path and image_path.exists():
                    pokemon_image = ctk.CTkImage(
                        dark_image=Image.open(image_path),
                        light_image=Image.open(image_path),
                        size=(150, 150)
                    )
                else:
                    pokemon_image = None

            button: ctk.CTkButton = ctk.CTkButton(
                self,
                text=f"{result_names[i]}",
                image=pokemon_image,
                height=200,
                width=200,
                compound="top",
                command=self.create_command(result_names[i])
            )
            button.name = name
            button.grid(row=row, column=col, padx=padding_x, pady=padding_y)
            i += 1

    def go_back(self) -> None:
        from views.home_view import HomeView
        self.master.show_view(HomeView)


    def create_command(self, poke_name: str) -> Callable[[], None]:
        return lambda: self.show_popup(poke_name)

    def show_popup(self, poke_name) -> None:
        pokemon_names = self.SearchModel.poke_on_click_handler(self.name)

        popup = ctk.CTkToplevel(self.master)
        popup.title(f"Select a Pokémon")
        popup.geometry("200x300")

        label = ctk.CTkLabel(
            popup, 
            text=f"Select a Pokémon to replace with {poke_name}:"
        )
        label.pack(pady=10)

        for i, name in enumerate(pokemon_names):
            button = ctk.CTkButton(
                popup, 
                text=name, 
                command=self.create_update_command(name, poke_name, popup)  # Pass popup here
            )
            button.pack(pady=5)

    def create_update_command(self, pokemon_name: str, new_pokemon: str, popup) -> Callable[[], None]:
        return lambda: self.update_and_close_popup(pokemon_name, new_pokemon, popup)

    def update_and_close_popup(self, pokemon_name: str, new_pokemon: str, popup) -> None:
        self.SearchModel.update_pokemon(pokemon_name, new_pokemon)
        popup.destroy()

