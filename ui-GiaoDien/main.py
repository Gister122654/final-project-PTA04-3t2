from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget
from PyQt6 import uic
import sys
class Login(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("ui-GiaoDien/login.ui", self)
        self.btnLogin.clicked.connect(self.checkLogin)
    def checkLogin(self):
        if self.txtEmail.text() == "SkibidiGooner" and self.txtPassword.text() == "skibidop":
            self.close()
if __name__ == "__main__":
    app = QApplication(sys.argv)
    lg = Login()
    lg.show()
    app.exec()