from curses import noraw
from typing import Union
from warnings import resetwarnings
import pandas as pd
from enum import Enum
from utils.helper import Helper
from utils.error_codes import ErrorCodes
import json
from pathlib import Path


class HomeModel:
    def __init__(self) -> None:
        self.Helper = Helper()

    def poke_on_click_handler(self, button: str) -> None:
        message: dict[str, str] = {
            "Title": "Add Pokemon",
            "Message": "Use the search bar to search for and add a pokemon"
        }
        Helper.show_popup(message)

    def search_pokemon(self, query: str) -> None:
       result: list[tuple[str, int]] = Helper.fuzzy_find(query)
       result_dir: Path = Path.cwd() / "data" / "pokemon.csv"

       with open(result_dir, "w") as file:
           json.dump(result, file)
