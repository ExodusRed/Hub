import tkinter as tk


class Menu(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__()
        self.create_widgets()

    def create_widgets(self):
        main_label = tk.Label(self, text="X")
        main_label.grid()