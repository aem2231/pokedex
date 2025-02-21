import customtkinter as ctk
from models.account_manager import AccountManager
from utils.helper import Helper

class LoginView(ctk.CTkFrame):
    def __init__(self, master) -> None:
        super().__init__(master)
        self.master = master
        self.AccountManager = AccountManager()
        self.create_ui()
        self.pack(expand=True, fill="both")


    def create_ui(self) -> None:
        self.username_label = ctk.CTkLabel(self, text="Username:")
        self.username_label.pack(pady=10)
        self.entry_username = ctk.CTkEntry(self, width=200)
        self.entry_username.pack(pady=5)

        self.password_label = ctk.CTkLabel(self, text="Password:")
        self.password_label.pack(pady=10)
        self.entry_password = ctk.CTkEntry(self, width=200, show="*")
        self.entry_password.pack(pady=5)

        self.login_button = ctk.CTkButton(self, text="Login", command=self.on_login_button_click)
        self.login_button.pack(pady=10)

        self.switch_to_signup_button = ctk.CTkButton(self, text="Don't have an account? Click here to signup.", command=self.switch_to_signup)
        self.switch_to_signup_button.pack(pady=10)

    def on_login_button_click(self) -> None:
        username: str = self.entry_username.get()
        password: str  = self.entry_password.get()

        r: int = self.AccountManager.validate_user(username, password)
        if r == 0:
            Helper.show_popup("Error", "Username or password is incorrect")
        if r == 1:
            from views.home_view import HomeView
            self.master.show_view(HomeView)
        if r == 2:
            Helper.show_popup("Error", "User does not exist")

    def switch_to_signup(self) -> None:
        from views.signup_view import SignupView
        self.master.show_view(SignupView)
