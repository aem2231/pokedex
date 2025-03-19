from api.pokemon import Pokemon
from utils.helper import Helper
import customtkinter as ctk
from typing import Union, Optional
from pathlib import Path
import json
from fuzzywuzzy import fuzz
from fuzzywuzzy import process
from PIL import Image
import urllib.request
import requests
import pandas as pd

class SearchModel(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        self.helper = Helper()
        self.pokemon_data_dir = Path.cwd() / "data" / "pokemon.json"
        self.master = master
        try:
            with open(self.pokemon_data_dir, "r") as f:
                self.data = json.load(f)
        except (FileNotFoundError, json.JSONDecodeError) as e:
            print(f"Failed to load Pokemon data: {e}")
            self.data = {"results": []}

    def search_pokemon(self, query: str) -> list:
        result: list[tuple[str, int]] = Helper.fuzzy_find(query)
        print(result)
        pokemon_names: list = []
        for i in result:
            pokemon_names.append(i[0])
            print(i)
        return pokemon_names

    def extract_id(self, url: str) -> int:
        try:
            id_str = url.rstrip('/').split('/')[-1]
            return int(id_str)
        except (ValueError, IndexError):
            return 0

    def get_results(self, results: list[tuple[str, int]]) -> list[str]:
        results_names: list[str] =[]
        i: int = 0
        for r in results:
            results_names.append(r[i])
            print(r[i])
        return results_names

    def poke_on_click_handler(self, name) -> list[str]:
        path_to_user_data: Path = Path.cwd() / "data" / "user_data.csv"
        user_data = pd.read_csv(path_to_user_data)
        pokemon_columns = ['Poke1', 'Poke2', 'Poke3', 'Poke4', 'Poke5', 'Poke6']
        pokemon_data = user_data.loc[user_data['Username'] == self.helper.get_username(), pokemon_columns].astype(str)
        pokemon = pokemon_data.values.flatten().tolist()

        pokemon_names = self.helper.get_pokemon_names(pokemon)

        return pokemon_names

    def get_image(self, name: str) -> Optional[Path]:
        try:
            url = f"https://pokeapi.co/api/v2/pokemon/{name}"
            print(url)
            response = requests.get(url)
            response.raise_for_status()  # Ensure the request was successful
            data = response.json()
            id_url = data["forms"][0]["url"]
            id = data["id"]

            image_url = f"https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/{id}.png"
            print(image_url)
            image_path = Path.cwd() / "data" / "images" / f"poke{id}.png"

            # Download the image if it doesn't already exist
            if not image_path.exists():
                urllib.request.urlretrieve(image_url, image_path)

            return image_path
        except Exception as e:
            print(f"Failed to get Pokemon image for {name}: {e}")
            return None



    def update_pokemon(self, pokemon_name: str, new_pokemon: str) -> None:
        # this function is more of a mess than my mental health /j

        old_url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_name}"
        result = requests.get(old_url)
        result.raise_for_status()
        data = result.json()
        old_id = data["id"]

        new_url = f"https://pokeapi.co/api/v2/pokemon/{new_pokemon}"
        result = requests.get(new_url)
        result.raise_for_status()
        data = result.json()
        new_id = data["id"]

        try:
            path_to_user_data: Path = Path.cwd() / "data" / "user_data.csv"
            user_data = pd.read_csv(path_to_user_data)

            pokemon_columns = ['Poke1', 'Poke2', 'Poke3', 'Poke4', 'Poke5', 'Poke6']
            username = self.helper.get_username()
            user_row = user_data.loc[user_data['Username'] == username, pokemon_columns]

            if user_row.empty:
                print(f"No Pokémon data found for user: {username}")
                return

            updated_row = user_row.replace({old_id: new_id}, regex=False)
            if updated_row.equals(user_row):
                print(f"Pokémon {old_id} not found in user data for user: {username}")
                return

            user_data.loc[user_data['Username'] == username, pokemon_columns] = updated_row.values
            user_data.to_csv(path_to_user_data, index=False)

        except FileNotFoundError:
            print(f"User data file not found at: {path_to_user_data}")
        except Exception as e:
            print(f"An error occurred while updating Pokémon: {e}")
