from PyQt5 import QtWidgets, uic
import sys


class GUI(QtWidgets.QMainWindow):
    def __init__(self):
        super(GUI, self).__init__()
        uic.loadUi("./ui_files/main.ui", self)
        self.univers: QtWidgets.QCheckBox = self.findChild(QtWidgets.QCheckBox, "checkBox")
        self.show()


app = QtWidgets.QApplication(sys.argv)
window = GUI()
app.exec_()
