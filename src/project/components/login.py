from tkinter import Misc, Frame, Tk, PhotoImage, Label
from pathlib import Path
from PIL import ImageTk, Image
from utils import position_window
from constants import WIDTH, HEIGHT, LOGIN_IMAGE

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

class ImageLabel(Label):
    def __init__(self) -> None:
        super().__init__()
        self._image = None
        
        self.create_image(LOGIN_IMAGE)
        self._config()

    def _config(self) -> None:
        self.config(
            background= "#06D6A0",
            image= f"{self._image}",
        )
    
    def create_image(self, image_login: Path) -> None:
        self._image = Image.open(image_login)
        self._image = self._image.resize((250,250))
        self._image = ImageTk.PhotoImage(self._image)
        

if __name__ == "__main__":
    root = LoginRoot()
    app = LoginWindow(root)
    label = ImageLabel()
    label.grid(row=0, column=0)
    app.mainloop()  