from typing import Union
import pandas as pd
from enum import Enum
from utils.helper import Helper
from utils.error_codes import ErrorCodes

class HomeModel:
    def __init__(self) -> None:
        self.Helper = Helper()

    def poke_on_click_handler(self, button: str) -> None:
        print(f"{button} clicked.")

    def search(self, query: str) -> None:
        print(f"search button clicked: {query}")
