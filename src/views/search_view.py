from utils.helper import Helper
import customtkinter as ctk
from typing import Callable
from models.search_model import SearchModel
from models.home_model import HomeModel
from PIL import Image

class SearchView(ctk.CTkFrame):
    def __init__(self, master) -> None:
        super().__init__(master)
        self.master = master
        self.SearchModel = SearchModel(self)
        self.HomeModel = HomeModel(self)
        self.pokemon_results = getattr(self.master.current_view, 'pokemon_results', [])
        self.create_ui()
        self.pack(expand=True, fill="both")

    def create_ui(self) -> None:
        self.search_box: ctk.CTkEntry = ctk.CTkEntry(self, width=300, placeholder_text="Search")
        self.search_box.grid(row=0, column=0, columnspan=3, padx=10, pady=10, sticky="n")

        search_button: ctk.CTkButton = ctk.CTkButton(self, text="Search", command=self.start_search())
        search_button.grid(row=0, column=2, columnspan=2, padx=10, pady=10, sticky="n")


        # Configure grid columns
        for i in range(5):  # 5 columns for 5 Pokémon per row
            self.grid_columnconfigure(i, weight=1)

        back_button: ctk.CTkButton = ctk.CTkButton(
            self,
            text="Back",
            command=self.go_back,
            width=100
        )
        back_button.grid(row=0, column=0, padx=10, pady=10, sticky="nw")
        padding_x: int = 10
        padding_y: int = 10

        # Create buttons for each result
        for i, pokemon in enumerate(self.pokemon_results):
            row = (i // 5) + 2  # Start from row 2 (after search elements)
            column = i % 5      # Columns 0-4 (5 items per row)

            try:
                # load the image
                image_path = f"data/poke{i+1}.png"
                pokemon_image = ctk.CTkImage(
                    dark_image=Image.open(image_path),
                    light_image=Image.open(image_path),
                    size=(150, 150)
                )

                button = ctk.CTkButton(
                    self,
                    text=pokemon["name"].capitalize(),
                    image=pokemon_image,
                    compound="top",
                    height=200,
                    width=200,
                    command=lambda p=pokemon: self.select_pokemon(p)
                )
                button.grid(row=row, column=column, padx=padding_x, pady=padding_y)
            except Exception as e:
                print(f"Error loading Pokemon image: {e}")

    def select_pokemon(self, pokemon: dict) -> None:
        print(f"Selected Pokemon: {pokemon['name']}")

    def add_pokemon(self, pokemon_name: str, pokemon_sprite: str) -> bool:
        success: bool = HomeModel.add_pokemon(pokemon_name, pokemon_sprite)
        return success

    def go_back(self) -> None:
        from views.home_view import HomeView
        self.master.show_view(HomeView)

    def start_search(self) -> Callable[[], None]:
        return lambda: self.switch_to_search_view()

    def switch_to_search_view(self) -> None:
        query = self.search_box.get()
        if query != "":  # Only search if there's a query
            print("search clicked")
            self.HomeModel.search_pokemon(query)
            from views.search_view import SearchView
            self.master.show_view(SearchView)
