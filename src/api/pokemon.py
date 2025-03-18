import requests
import os
from pathlib import Path
from utils.error_codes import ErrorCodes
from typing import Dict, Optional
import urllib.request
from PIL import Image

class Pokemon:
    @classmethod
    def get_pokemon(cls) -> dict[str, list[dict[str, str]]]:  # Fixed return type
        url: str = "https://pokeapi.co/api/v2/pokemon?limit=100000&offset=0"
        try:
            response = requests.get(url, timeout=50)
            response.raise_for_status()  # Raises error for bad status codes
            return response.json()
        except requests.RequestException as e:
            print(f"Failed to fetch Pokemon: {e}")
            return {"results": []}  # Return empty results instead of failing

    @classmethod
    def get_pokemon_image(cls, pokemon_id: int, result_num: int) -> Optional[Image.Image]:  # Added return type
        try:
            url = f"https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/{pokemon_id}.png"
            image_path = Path.cwd() / "data" / f"poke{result_num}.png"
            urllib.request.urlretrieve(url, image_path)
            return Image.open(image_path)
        except Exception as e:
            print(f"Failed to get Pokemon image: {e}")
            return None
