from typing import Union
from warnings import resetwarnings
import pandas as pd
from enum import Enum
from utils.helper import Helper
from utils.error_codes import ErrorCodes
import json
from pathlib import Path
import customtkinter as ctk
from models.search_model import SearchModel
from utils.helper import Helper


class HomeModel(ctk.CTkFrame):
    def __init__(self, master) -> None:
        super().__init__(master)
        self.Helper = Helper()
        self.SearchModel = SearchModel(self)

    def poke_on_click_handler(self, button: str) -> None:
        message: dict[str, str] = {
            "Title": "Add Pokemon",
            "Message": "Use the search bar to search for and swap a pokemon"
        }
        Helper.show_popup(message)

    def search_pokemon(self, query: str) -> list:
        result: list[tuple[str, int]] = Helper.fuzzy_find(query)
        print(result)
        return result

    def get_pokemon(self) -> list[str]:
        path_to_user_data: Path = Path.cwd() / "data" / "user_data.csv"
        user_data = pd.read_csv(path_to_user_data)
        pokemon_columns = ['Poke1', 'Poke2', 'Poke3', 'Poke4', 'Poke5', 'Poke6']
        pokemon_data = user_data.loc[user_data['Username'] == self.Helper.get_username(), pokemon_columns].astype(str)
        return pokemon_data.values.flatten().tolist()
