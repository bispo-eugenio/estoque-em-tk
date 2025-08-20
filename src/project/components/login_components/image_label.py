from tkinter import Label
from constants import LOGIN_IMAGE
from PIL import Image, ImageTk
from pathlib import Path

class ImageLabel(Label):

    def __init__(self) -> None:
        super().__init__()
        self._image = None
        
        self.create_image(LOGIN_IMAGE)
        self._config()

    def _config(self) -> None:
        self.config(
            background= "#06D6A0",
            image= f"{self._image}", #Passando como str -> erro de type
        )
    
    def create_image(self, image_login: Path) -> None:
        self._image = Image.open(image_login)
        self._image = self._image.resize((250,250))
        self._image = ImageTk.PhotoImage(self._image)