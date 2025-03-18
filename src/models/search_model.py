from api.pokemon import Pokemon
from utils.helper import Helper
import customtkinter as ctk
from typing import Union
from pathlib import Path
import json
from fuzzywuzzy import fuzz
from fuzzywuzzy import process

class SearchModel(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        self._helper = Helper()
        self.pokemon_data_dir = Path.cwd() / "data" / "pokemon.json"
        self.master = master
        try:
            with open(self.pokemon_data_dir, "r") as f:
                self.data = json.load(f)
        except (FileNotFoundError, json.JSONDecodeError) as e:
            print(f"Failed to load Pokemon data: {e}")
            self.data = {"results": []}

    def get_pokemon_data(self, result: list[tuple[str, int]]) -> list[dict]:
        i: int = 0
        pokemon_list = []
        for r in result: # O(m*n) time complecity :(
            i+=1
            name: str = r[0]
            for d in self.data.get("results", []):
                if d["name"] == name:
                    url: str = d["url"]
                    id: int = self.extract_id(url)
                    if id != 0:
                        Pokemon.get_pokemon_image(id, i)
                        pokemon_list.append({
                            "id": id, # 6 levels deep holy shit my eyes burn
                            "name": name,
                            "url": url
                        })
        return pokemon_list

    def extract_id(self, url: str) -> int:
        try:
            id_str = url.rstrip('/').split('/')[-1]
            return int(id_str)
        except (ValueError, IndexError):
            return 0
