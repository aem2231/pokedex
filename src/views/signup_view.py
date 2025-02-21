import customtkinter as ctk
from models.account_manager import AccountManager
from utils.helper import Helper
import bcrypt

class SignupView(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master
        self.AccountManager = AccountManager()
        self.create_ui()
        self.pack(expand=True, fill="both")

    def create_ui(self) -> None:
        self.email_label = ctk.CTkLabel(self, text="Email:")
        self.email_label.pack(pady=10)
        self.entry_email = ctk.CTkEntry(self, width=200)
        self.entry_email.pack(pady=5)

        self.username_label = ctk.CTkLabel(self, text="Username:")
        self.username_label.pack(pady=10)
        self.entry_username = ctk.CTkEntry(self, width=200)
        self.entry_username.pack(pady=5)

        self.password_label = ctk.CTkLabel(self, text="Password:")
        self.password_label.pack(pady=10)
        self.entry_password = ctk.CTkEntry(self, width=200, show="*")
        self.entry_password.pack(pady=5)

        self.signup_button = ctk.CTkButton(self, text="Sign Up", command=self.on_signup_button_click)
        self.signup_button.pack(pady=10)

        self.switch_to_login_button = ctk.CTkButton(self, text="Already have an account? Click here to login.", command=self.switch_to_login)
        self.switch_to_login_button.pack(pady=10)

    def on_signup_button_click(self) -> None:
        email = self.entry_email.get()
        username = self.entry_username.get()
        password = self.entry_password.get()

        r = self.AccountManager.validate_signup(email, username, password) # Here, r is just the return value
        if r == 3:
            Helper.show_popup("Error", "Email already exists")
        elif r == 4:
            Helper.show_popup("Error", "Username already exists")
        elif r == 5:
            Helper.show_popup("Error", "Invalid email")
        elif r in (6, 7, 8):
            Helper.show_popup("Error", f"{"email" if r == 6 else "username" if r == 7 else "password"} must not be empty.")
        elif r == 9:
            Helper.show_popup("Error", "Password must be at least 8 characters long.")
        else:
            print("Signup successful!")
            from views.home_view import HomeView
            self.master.show_view(HomeView)

    def switch_to_login(self) -> None:
        from views.login_view import LoginView
        self.master.show_view(LoginView)

    def hash_password(self, password: str) -> str:
        return bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
