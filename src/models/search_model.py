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

    def fuzzy_find(self, query: str):
        poke_data_path: Path = Path.cwd() / "data" / "pokemon.json"
        pokemon: list[str] = []
        with open(poke_data_path, "r") as f:
            data: dict[str, list[dict[str, str]]] = json.load(f)
            for p in data["results"]:
                pokemon.append(p["name"])

        result: list[tuple[str, int]] = process.extract(query, pokemon)
        self.get_pokemon_ids(result)

    def get_pokemon_ids(self, result: list[tuple[str, int]]) -> None:
        data: dict = {}
        with open(Path.cwd() / "data" / "pokemon.json", "r") as f:
            data = json.load(f)

        ids: list[int] = []
        for name, _ in result:
            for p in data["results"]:
                if p["name"] == name:
                    ids.append(p["id"])
        print(ids)
