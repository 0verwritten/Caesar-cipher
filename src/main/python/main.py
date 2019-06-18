from fbs_runtime.application_context.PyQt5 import ApplicationContext
from PyQt5 import QtWidgets,QtCore,QtGui

from src.main.python.design import Ui_MainWindow
import sys


class MainApp(QtWidgets.QApplication, Ui_MainWindow):
    def __init__(self):
        super(MainApp, self).__init__([])
        self.mainwindow = QtWidgets.QMainWindow()
        self.setupUi(self.mainwindow)
        self.lineEdit
        self.pushButton_2.pressed.connect(self.add)
        self.pushButton.pressed.connect(self.remove)
        self.mainwindow.show()
    def add(self):
        self.lineEdit.setText(str(int(self.lineEdit.text())+1))
    def remove(self):
        self.lineEdit.setText(str(int(self.lineEdit.text())-1))


if __name__ == '__main__':
    window = MainApp()
    sys.exit(window.exec())