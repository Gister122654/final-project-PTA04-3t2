from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget # them widget từ pyqt6
from PyQt6 import uic # them chuc nang load ui
import sys # them thu vien dieu khien he thong

#lop Trang Chu
class HomeDashboard(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("ui-GiaoDien/home.ui", self)
        # nut de ve trang chu
        self.btnHome.clicked.connect(self.showHome)
        # nut de mo thong tin ca nhan
        self.btnProfile.clicked.connect(self.showProfile)
    
    def showHome(self):
        self.stackedMenu.setCurrentIndex(1)
    def showProfile(self):
        self.stackedMenu.setCurrentIndex(2)

#Lop Dang Ky
class SignUp(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("UI-GiaoDien/Signup.ui", self)
        # them su kien khi nhan vao nut dang ky
        self.btnSignUp.clicked.connect(self.registerAccount)
        self.btnLogin.clicked.connect(self.showLogin)
    def showLogin(self):
        self.close()
        lg.show()

    def registerAccount(self):
        # doc thong tin nguoi dung nhap vao
        username = self.txtUserName
        password = self.txtPassWord
        confirmPassword = self.txtConfirmPassWord
        # neu chua nhap thi cho nguoi dung nhap
        if  username.text() == "":
            username.setFocus()
            return
        if password.text() == "":
            password.setFocus()
            return
        if confirmPassword.text() == "":
            confirmPassword.setFocus()
            return
        # neu nhu email khong dung dinh dang
        if username.text().find("@gmail.com") == -1:
            username.clear()
            username.setFocus()
            return
        # neu nhu mat khau va nhap lai mat khau khong dung
        if password.text() != confirmPassword.text():
            confirmPassword.setFocus()
            return

        # them tai khoan moi vao file 
        with open("accounts.txt", "a") as file:
            file.write(username.text() + ":" + password.text() + "\n")
        self.close()


# hien thi trang dang nhap
class Login(QMainWindow):
    # ham khoi tao giao dien UI
    def __init__(self):
        # khoi tao app
        super().__init__()
        # doc giao dien tu file login.ui
        uic.loadUi("UI-GiaoDien/login.ui", self)
        # khi nhan vao nut Login

        self.btnLogin.clicked.connect(self.checkLogin)
        self.btnSignup.clicked.connect(self.showSignup)
    def showSignup(self):
        self.close()
        su.show()
    def checkLogin(self):
        # mở file txt lên để đọc thông tin
        with open("accounts.txt", "r") as file:
            data = file.readlines()
            accounts = []
            for line in data:
                line = line.replace("\n", "")
                line = line.strip()
                accounts.append(line)
        # neu nhu tk va mk dung thi cho dang nhap
        if (self.txtEmail.text() + ":" + self.txtPassword.text()) in accounts:
            # dong trang dang nhap di
            self.close() 
            # mo trang chu ra
            home.show()

if __name__ == "__main__": # code se chay tu dong nay
    app = QApplication(sys.argv)
    lg = Login()
    su = SignUp()
    home = HomeDashboard()
    lg.show()
    app.exec() # giup app se lien tuc hoat dong, khong tat di

