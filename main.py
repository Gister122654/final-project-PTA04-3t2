from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget
from PyQt6 import uic
import sys
class SignUp(QMainWindow):
    def __init__(self, parent: QWidget | None = ..., flags: Qt.WindowType = ...) -> None:
        super().__init__()
        uic.loadUi("ui-GiaoDien/Signup.ui", self)
        self.btnSignUp.clicked.connect(self.registerAccount)
    def registerAccount(self):
        username = self.txtUserName
        password = self.txtPassWord
        confirmPassword = self.txtConfirmPassWord
        #neu chua nhap thi cho ng dung nhap:
        if username.text() == "":
            username.setFocus()
            return
        if password.text() == "":
            password.setFocus()
            return
        if confirmPassword.text()== "":
            confirmPassword.setFocus()
            return
        if username.text().find("@gmail.com") == -1:
            username.clear()
            username.setFocus()
            return
        if password.text() != confirmPassword.text():
            confirmPassword.setFocus()
            return
class Login(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("ui-GiaoDien/login.ui", self)
        self.btnLogin.clicked.connect(self.checkLogin)
    def checkLogin(self):
        with open("account.txt", "r") as file:
            data = file.readlines()
            accounts = []
            for line in data:
                line = line.replace("\n", "")
                line = line.strip()
                accounts.append(line)
        if (self.txtEmail.text() + ":" + self.txtPassword.text()) in accounts:
            self.close()
if __name__ == "__main__":
    app = QApplication(sys.argv)
    lg = Login()
    su = SignUp()
    su.show()
    # lg.show()
    app.exec()