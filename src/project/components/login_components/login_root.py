from tkinter import Tk
from utils import position_window
from constants import WIDTH, HEIGHT

class LoginRoot(Tk):
    def __init__(self) -> None:
        super().__init__()
        self._position_x = position_window(self.winfo_screenwidth(), WIDTH)
        self._position_y = position_window(self.winfo_screenheight(), HEIGHT)
        self._config()
    
    def _config(self) -> None:
        self.title("Login")
        # self.iconbitmap # Colocar depois
        self.geometry(f"{WIDTH}x{HEIGHT}+{self._position_x}+{self._position_y}")
        self.resizable(False, False)