import customtkinter as ctk
from models.account_manager import AccountManager
from utils.helper import Helper

class SignupView(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master
        self.AccountManager = AccountManager()
        self.Helper = Helper()
        self.create_ui()
        self.pack(expand=True, fill="both")

    def create_ui(self) -> None:
        email_label = ctk.CTkLabel(self, text="Email:")
        email_label.pack(pady=10)
        entry_email = ctk.CTkEntry(self, width=200)
        entry_email.pack(pady=5)

        username_label = ctk.CTkLabel(self, text="Username:")
        username_label.pack(pady=10)
        entry_username = ctk.CTkEntry(self, width=200)
        entry_username.pack(pady=5)

        password_label = ctk.CTkLabel(self, text="Password:")
        password_label.pack(pady=10)
        entry_password = ctk.CTkEntry(self, width=200, show="*")
        entry_password.pack(pady=5)

        signup_button = ctk.CTkButton(self, text="Sign Up", command=lambda: self.on_signup_button_click(entry_email, entry_username, entry_password))
        signup_button.pack(pady=10)

        switch_to_login_button = ctk.CTkButton(self, text="Already have an account? Click here to login.", command=self.switch_to_login)
        switch_to_login_button.pack(pady=10)

    def on_signup_button_click(self, entry_email, entry_username, entry_password) -> None:
        email = entry_email.get()
        username = entry_username.get()
        password = entry_password.get()

        error = self.AccountManager.validate_signup(email, username, password)
        message = self.Helper.error_handler(error)
        if message == None:
            Helper.start_session(username)
            from views.home_view import HomeView
            self.master.show_view(HomeView)
        else:
            Helper.show_popup(message)

    def switch_to_login(self) -> None:
        from views.login_view import LoginView
        self.master.show_view(LoginView)
