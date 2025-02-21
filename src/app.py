import customtkinter as ctk
from utils.helper import Helper
from views.login_view import LoginView
from views.signup_view import SignupView

class MainApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Pokédex App")
        self.geometry("400x300")

        self.current_view = LoginView(self)

    def show_view(self, view_class):
        """Switch to a different view by destroying the current view."""
        if self.current_view is not None:
            self.current_view.destroy()  # Destroy the current view if it exists

        # Create a new view and pack it
        self.current_view = view_class(self)
        self.current_view.pack(expand=True, fill="both")

if __name__ == "__main__":
    Helper.start()
    app = MainApp()
    app.mainloop()
