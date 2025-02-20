import customtkinter as ctk
from models.user_functions import UserFunctions
from views.login_view import LoginView

# Create the main window (root)
root = ctk.CTk()

# Initialize and show the LoginView
login_view = LoginView(root)

# Run the Tkinter event loop
root.mainloop()
