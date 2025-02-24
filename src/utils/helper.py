from email.policy import default
from pathlib import Path
import pandas as pd
from typing import Union, Optional, Dict, Mapping
import customtkinter as ctk
import bcrypt
import json

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
                user_data_file.write_text("Email,Username,Password,Poké1,Poké2,Poké3,Poké4,Poké5,Poké6\n")
                print(f"Created new data file at {user_data_file}")
        except Exception as e:
            print(f"An error occurred while trying to create the data file: {e}")

    @classmethod
    def load_config(cls) -> Mapping[str, Union[str, Path]]:
        """Loads the config

        Returns:
            - Mapping[str, Union[str, Path]]"""
        config: Mapping[str, Union[str, Path]] = {}
        try:
            config_file: Path = Path.cwd() / "config" / "config.jsonc"
            config_file.parent.mkdir(parents=True, exist_ok=True)
            theme_path: Path = Path.cwd() / "themes" / "catppuccin-mocha.json"
            default_config: Dict[str, str] = {
                "appearance_mode": str(theme_path),
                "color_theme": str(theme_path)
            }

            if not config_file.exists():
                with open(config_file, "w") as file:
                    json.dump(default_config, file, indent=4)
                print(f"Created new config file at {config_file}")
                return default_config
            else:
                with open(config_file, "r") as file:
                    config = json.load(file)
                return config
        except Exception as e:
            print(f"An error occurred while trying to create the data file: {e}")
            return default_config

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
    def get_username(cls) -> str:
        """Returns username"""
        with open("session.json", "r") as session_file:
            data = json.load(session_file)
            return data["username"]

    # This method is purely for the greetings in views/home_view.py to work
    @classmethod
    def start_session(cls, username: str) -> None:
        with open("session.json", "w") as session_file:
            json.dump({"username": username}, session_file, indent=4)

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
