from tkinter import Frame, Misc
from constants import WIDTH, HEIGHT

class LoginWindow(Frame):
    def __init__(self, master: Misc | None = None) -> None:
        super().__init__(master)
        self._config()
        self.grid()

    def _config(self) -> None:
        self.config(
            background= "#06D6A0",
            width= WIDTH,
            height= HEIGHT,
            )