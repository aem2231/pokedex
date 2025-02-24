import customtkinter as ctk
from models.account_manager import AccountManager
from utils.helper import Helper

class LoginView(ctk.CTkFrame):
    def __init__(self, master) -> None:
        super().__init__(master)
        self.master = master
        self.AccountManager = AccountManager()
        self.Helper = Helper()
        self.create_ui()
        self.pack(expand=True, fill="both")

    def create_ui(self) -> None:
        username_label = ctk.CTkLabel(self, text="Username:")
        username_label.pack(pady=10)
        entry_username = ctk.CTkEntry(self, width=200)
        entry_username.pack(pady=5)

        password_label = ctk.CTkLabel(self, text="Password:")
        password_label.pack(pady=10)
        entry_password = ctk.CTkEntry(self, width=200, show="*")
        entry_password.pack(pady=5)

        login_button = ctk.CTkButton(self, text="Login", command=lambda: self.on_login_button_click(entry_username, entry_password))
        login_button.pack(pady=10)

        switch_to_signup_button = ctk.CTkButton(self, text="Don't have an account? Click here to signup.", command=self.switch_to_signup)
        switch_to_signup_button.pack(pady=10)

    def on_login_button_click(self, entry_username: ctk.CTkEntry, entry_password: ctk.CTkEntry) -> None:
        username: str = entry_username.get()
        password: str  = entry_password.get()

        error = self.AccountManager.validate_user(username, password)
        message = self.Helper.error_handler(error)
        if message is None:
            Helper.start_session(username)
            from views.home_view import HomeView
            self.master.show_view(HomeView)
        else:
            Helper.show_popup(message)

    def switch_to_signup(self) -> None:
        from views.signup_view import SignupView
        self.master.show_view(SignupView)
