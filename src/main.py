from project.components.main_window import MainWindow
from tkinter import * #type: ignore

def main() -> None:
    root = Tk()
    app = MainWindow(root)
    app.mainloop()


if __name__ == "__main__":
    main()