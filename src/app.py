import customtkinter as ctk
from utils.helper import Helper
from views.login_view import LoginView

# this code is the definition of 'if it ain't broke, don't fix it'
# i'm not going to touch it most of it with a 10-foot pole to prevent myself from going insane (i already am)
# theres probably some redundant functions or methods, whiicch i won't toich out of fear of breaking eveything
# i'm sorry


# this class is probably fine actually, but everything else is a mess (good luck)
class MainApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Pokédex App")
        self.geometry("700x900")
        self.current_view = None
        Helper.start()
        self.show_view(LoginView)

        ctk.set_appearance_mode("dark")


    def show_view(self, view_class):
        if self.current_view:
            self.current_view.destroy()
        self.current_view = view_class(self)
        self.current_view.pack(expand=True, fill="both")

if __name__ == "__main__":
    app = MainApp()
    app.mainloop()
