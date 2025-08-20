from login_components.login_root import LoginRoot
from login_components.login_window import LoginWindow
from login_components.image_label import ImageLabel



def login_acess() -> None:
    root = LoginRoot()
    app = LoginWindow(root)
    label = ImageLabel()
    label.grid(row=0, column=0)
    app.mainloop()  


if __name__ == "__main__":
    login_acess()