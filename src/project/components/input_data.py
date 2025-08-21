from tkinter import Entry, Tk
from typing import Any
from utils import empty


class InputData(Entry):

    def __init__(self, master: Any = None,  # noqa: ANN401
        placeholder: str = "PLACEHOLDER", color: str = "gray") -> None:
        super().__init__(master)

        self.placeholder = placeholder
        self.color_placeholder = color
        self._default_color = self["fg"]

        #Configura o bind/evento de focus in e focus out
        self.bind("<FocusIn>", self._foc_in)
        self.bind("<FocusOut>", self._foc_out)

        #Cria o placeholder quando inicializar
        self.create_placeholder()


    def create_placeholder(self) -> None:
        if empty(self.get()):
            self["fg"] = self.color_placeholder
            self.insert(0, self.placeholder)

    #Configuração de Eventos
    
    def _foc_in(self, *args: Any) -> None: #noqa: ANN401
        if not empty(self.get()):
            self.delete(0, "end")
            self["fg"] = self._default_color

    def _foc_out(self, *args: Any) -> None: #noqa: ANN401
        if empty(self.get()):
            self.create_placeholder()

if __name__ == "__main__":
    root = Tk()
    username = InputData(root, placeholder="Username")
    password = InputData(root, placeholder="Password")
    username.grid(row=0, column=0)
    password.grid(row=1, column=0)
    root.mainloop()