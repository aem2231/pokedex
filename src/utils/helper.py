from email.policy import default
from pathlib import Path
import pandas as pd
from typing import Union, Optional, Dict, Mapping
import customtkinter as ctk
import bcrypt
import json
from fuzzywuzzy import fuzz
from fuzzywuzzy import process
from api.pokemon import Pokemon
import random
import requests

class Helper:
    @classmethod
    def get_user_data_path(cls) -> Path:
        """Returns data directory as a Path"""
        return Path.cwd() / "data" / "user_data.csv"

    @classmethod
    def start(cls) -> None:
        """Start function that is ran every time the program is launched."""
        # Create the data file if it doesn't exist
        try:
            user_data_file: Path = Path.cwd() / "data" / "user_data.csv"
            user_data_file.parent.mkdir(parents=True, exist_ok=True)

            if not user_data_file.exists():
                user_data_file.write_text("Email,Username,Password,Poke1,Poke2,Poke3,Poke4,Poke5,Poke6\n")
                print(f"Created new data file at {user_data_file}")
        except Exception as e:
            print(f"An error occurred while trying to create the data file: {e}")

        try:
            images_file_path: Path = Path.cwd() / "data" / "images"
            images_file_path.mkdir(parents=True, exist_ok=True)
        except Exception as e:
            print(f"An error occured: {e}")

        # load all pokemon names into a json if it doesn't exist'
        try:
            pokemon_file: Path = Path.cwd() / "data" / "pokemon.json"
            pokemon_file.parent.mkdir(parents=True, exist_ok=True)

            if not pokemon_file.exists():
                pokemon_data: dict[str, str] = Pokemon.get_pokemon()
                with open(pokemon_file, "w") as file:
                    json.dump(pokemon_data, file, indent=4)
        except Exception as e:
            print(f"Failed to load pokemon: {e}")
            return None

    @classmethod # i dont actually remember why i put this function here, but fuck it we ball
    def fuzzy_find(cls, query) -> list[tuple[str, int]]:
        poke_data_path: Path = Path.cwd() / "data" / "pokemon.json"
        pokemon: list[str] = []
        with open(poke_data_path, "r") as f:
            data: dict[str, list[dict[str, str]]] = json.load(f)
            for p in data["results"]:
                pokemon.append(p["name"])

        result: list[tuple[str, int]] = process.extract(query, pokemon, limit = 10)

        names: list[str] = []
        i: int = 0
        for r in result:
            names.append(r[i])

        return names

    @classmethod
    def show_popup(cls, message: Dict[str, str]) -> None:
        """Shows a popup message.

        Paramaters:
            - Dict [str, str]"""
        title: str = message["Title"]
        content: str = message["Message"]

        popup = ctk.CTkToplevel()
        popup.title(title)
        popup.geometry("300x100")

        label = ctk.CTkLabel(popup, text=content)
        label.pack(pady=10)

        button = ctk.CTkButton(popup, text="OK", command=popup.destroy)
        button.pack(pady=10)

    @classmethod
    def hash_password(cls, password: str) -> str:
        return bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()

    @classmethod
    def start_session(cls, username: str) -> None:
        try:
            with open("session.json", "w") as session_file:
                json.dump({"username": username}, session_file, indent=4)
        except Exception as e:
            print(f"Failed to create session: {e}")

    @classmethod
    def get_username(cls) -> str:
        try:
            with open("session.json", "r") as session_file:
                data = json.load(session_file)
                return data.get("username", "User")  # Default to "User" if not found
        except Exception as e:
            print(f"Failed to get username: {e}")
            return "User"

    @classmethod
    def error_handler(cls, error_code: int) -> Optional[Dict[str, str]]:
        """Error handler

        Paramaters:
            - error_code (int)

        Returns:
            - message:  A dict of 'title' and 'content'
            - None:  Returns on success"""
        message: Dict[str, str] = {"Title": "Message", "Message": ""}
        if error_code == 0:
            message["Message"] = "Username or password is incorrect"
        elif error_code == 1:
            message["Message"] = "User not found"
        elif error_code == 2:
            message["Message"] = "User already exists"
        elif error_code == 3:
            message["Message"] = "Invalid email"
        elif error_code == 4:
            message["Message"] = "Invalid username"
        elif error_code == 5:
            message["Message"] = "Password must be at least 8 digits"
        elif error_code == 6:
            message["Message"] = "Email already exists"
        elif error_code == 7:
            return None
        return message

    @classmethod
    def get_pokemon_names(cls, pokemon_ids: list[int]) -> list[str]:
        """Retrieve Pokémon names for a given list of Pokémon IDs."""
        try:
            # Fetch Pokémon names using the API
            pokemon_names = []
            for poke_id in pokemon_ids:
                if pd.notna(poke_id):  # Ensure the ID is not NaN
                    url = f"https://pokeapi.co/api/v2/pokemon/{int(poke_id)}"
                    response = requests.get(url)
                    if response.status_code == 200:
                        pokemon_data = response.json()
                        # Access the "name" key directly from the response
                        pokemon_names.append(pokemon_data["name"])
                    else:
                        print(f"Failed to fetch data for Pokémon ID {poke_id}")

            return pokemon_names
        except Exception as e:
            print(f"An error occurred: {e}")
            return []


    @classmethod
    def get_result_names(cls, result_name: list[str]) -> list[str]:
        return result_names

    @classmethod
    def save_result_names(cls, result_names: list[str]) -> None:
        # wtf

        results = {
            "result": result_names
        }

        print(result_names)

        try:
            with open("result_names.json", "w") as f:
                json.dump(results, f, indent=4)
        except Exception as e:
            print(f"Failed to save result names: {e}")

    @classmethod
    def load_result_names(cls) -> list[str]:
        """Load the list of result names from a JSON file.""" # ???
        try:
            with open("result_names.json", "r") as f:
                return json.load(f)["result"]
        except FileNotFoundError:
            print("Result names file not found. Returning an empty list.")
            return []
        except Exception as e:
            print(f"Failed to load result names: {e}")
            return []

    @classmethod
    def get_placeholder_image(cls) -> Optional[Path]:
        try:
            return Path.cwd() / "assets" / "placeholder.png"
        except Exception as e:
            print(f"Failed to load placeholder image: {e}")
            return None
