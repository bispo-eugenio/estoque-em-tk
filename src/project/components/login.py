from login_components.login_root import LoginRoot
from login_components.login_window import LoginWindow
from login_components.image_label import ImageLabel
from tkinter import Label
from input_data import InputData



def login_acess() -> None:
    root = LoginRoot()
    app = LoginWindow(root)
    label = ImageLabel(app) #Verificar
    username = InputData(root, "Username")
    password = InputData(root, "Password")
    label.grid(row=0, column=0)
    username.grid(row=2, column=0)
    password.grid(row=4, column=0)

    app.mainloop()  


if __name__ == "__main__":
    login_acess()