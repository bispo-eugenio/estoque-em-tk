from tkinter import Entry, Tk
from typing import Any


class InputData(Entry):

    def __init__(self, master: Any = None,  # noqa: ANN401
        placeholder: str = "PLACEHOLDER", color: str = "gray") -> None:
        super().__init__(master)

        self.placeholder = placeholder
        self.color = color



if __name__ == "__main__":
    root = Tk()
    username = InputData(root, placeholder="Username")
    username.grid(row=0, column=0)
    root.mainloop()