from model.main_model import MainModel
from controller.main_controller import MainController
from view.menu_view import Menu
from view.settings_view import Settings

from style import Style

import tkinter as tk


class Hub(tk.Tk):
    def __init__(self, style):
        super().__init__()
        self.title("Hub")
        self.geometry("640x480")

        self.container = tk.Frame(self)
        # self.pack(fill="both", expand=True)

        self.model = MainModel()
        self.views = {Menu}
        self.controller = MainController()

        self.frames = {}

        for F in (Menu, Settings):
            frame = F(self.container, self, style)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(Menu)

    def show_frame(self, view_class):
        frame = self.frames[view_class]
        frame.tkraise()

    def toggle_dark_mode(self):
        self.model.toggle_dark_mode()
        print("Dark Mode", self.model.settings["dark_mode"]) # Test


if __name__ == "__main__":
    style = Style(bg="grey12", fg="white", font="Lucida Console", font_size=18)
    hub = Hub(style)
    hub.mainloop()

