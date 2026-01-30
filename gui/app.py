import customtkinter as ctk
from gui.widgets import ChatWidgets

def start_gui():
    ctk.set_appearance_mode("dark")
    ctk.set_default_color_theme("blue")

    app = ctk.CTk()
    app.title("Cherry AI 🍒")
    app.geometry("1000x750")

    ChatWidgets(app)

    app.mainloop()
