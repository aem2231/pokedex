from enum import STRICT
import requests
import os
from pathlib import Path
from utils.error_codes import ErrorCodes

class Pokemon:
    def __init__(self) -> None:
        ...

    @classmethod
    def get_pokemon(cls) -> dict[str, str]:
        url: str = "https://pokeapi.co/api/v2/pokemon?limit=100000&offset=0"
        response = requests.get(url, timeout=50)
        pokemon_data_global = response.json()
        return pokemon_data_global
