import tkinter as tk


class Settings(tk.Frame):
    def __init__(self, parent, controller, style):
        super().__init__()
        self.create_widgets()

    def create_widgets(self):
        settings_label = tk.Label(self, text="Settings")
        settings_label.grid()