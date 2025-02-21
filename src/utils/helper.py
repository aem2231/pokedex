from pathlib import Path
import customtkinter as ctk
import bcrypt

class Helper:
    @classmethod
    def get_user_data_path(cls):
        return Path.cwd() / "data" / "user_data.csv"

    @classmethod
    def start(cls):
        try:
            user_data_file = Path.cwd() / "data" / "user_data.csv"
            user_data_file.parent.mkdir(parents=True, exist_ok=True)

            if not user_data_file.exists():
                user_data_file.write_text("Email,Username,Password,Poké1,Poké2,Poké3,Poké4,Poké5,Poké6\n")
                print(f"Created new data file at {user_data_file}")
        except Exception as e:
            print(f"An error occured while trying to create the data file: {e}")

    @classmethod
    def show_popup(cls, title: str, message: str):
        popup = ctk.CTkToplevel()
        popup.title(title)
        popup.geometry("200x100")

        label = ctk.CTkLabel(popup, text=message)
        label.pack(pady=10)

        button = ctk.CTkButton(popup, text="OK", command=popup.destroy)
        button.pack(pady=10)

    @classmethod
    def hash_password(cls, password: str) -> str:
        return bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
