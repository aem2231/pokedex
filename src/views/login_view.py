import customtkinter as ctk
from models.user_functions import UserFunctions

class LoginView:
    def __init__(self, root):
        self.root = root
        self.root.title("Login")
        self.root.geometry("300x200")
        self.create_ui()
        self.user_functions = UserFunctions()

    def create_ui(self):
        self.username_label = ctk.CTkLabel(self.root, text="Username:")
        self.username_label.pack(pady=10)
        self.entry_username = ctk.CTkEntry(self.root, width=200)
        self.entry_username.pack(pady=5)

        self.password_label = ctk.CTkLabel(self.root, text="Password:")
        self.password_label.pack(pady=10)
        self.entry_password = ctk.CTkEntry(self.root, width=200, show="*")
        self.entry_password.pack(pady=5)

        self.login_button = ctk.CTkButton(self.root, text="Login", command=self.on_login_button_click)
        self.login_button.pack(pady=10)

    def on_login_button_click(self):
        username = self.entry_username.get()
        password = self.entry_password.get()

        error_code = self.user_functions.validate_user(username, password)
        if error_code == 0:
            print("Password is incorrect")
        if error_code == 1:
            print("User and password match")
        if error_code == 2:
            print("No such user")
