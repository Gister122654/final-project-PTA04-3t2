from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget # them widget từ pyqt6
from PyQt6 import uic
import sys


class Home (QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("ui-GiaoDien/notehome.ui", self)
        self.btnCreate.clicked.connect(self.showCreate)
    def showCreate(self):
        note.show()
class Note (QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("ui-GiaoDien/note.ui", self)
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    home = Home()
    note = Note()
    home.show()
    app.exec()