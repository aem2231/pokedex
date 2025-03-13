import requests
import os
from pathlib import Path
from utils.error_codes import ErrorCodes
from typing import Dict

class Pokemon:
    def __init__(self) -> None:
        ...

    @classmethod
    def get_pokemon(cls) -> dict[str, str]:
        url: str = "https://pokeapi.co/api/v2/pokemon?limit=100000&offset=0"
        response = requests.get(url, timeout=50)
        pokemon_data_global = response.json()
        return pokemon_data_global

    @classmethod
    def get_pokemon_image(cls, pokemon_id: int) -> requests.Response:
        url: str = f"https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/{pokemon_id}.png"
        response: requests.Response = requests.get(url, timeout=50)
        response.raise_for_status()
        return response
