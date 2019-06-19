from fbs_runtime.application_context.PyQt5 import ApplicationContext
from PyQt5 import QtWidgets,QtCore,QtGui

from src.main.python.design import Ui_MainWindow
import sys


class MainApp(QtWidgets.QApplication, Ui_MainWindow):
    def __init__(self):
        super(MainApp, self).__init__([])
        self.mainwindow = QtWidgets.QMainWindow()
        self.setupUi(self.mainwindow)
        self.lineEdit.setValidator(QtGui.QIntValidator())
        self.pushButton_2.pressed.connect(self.add)
        self.pushButton.pressed.connect(self.remove)
        self.textBrowser.textChanged.connect(self.encrypt)
        self.mainwindow.show()
    def add(self):
        self.lineEdit.setText(str(int(self.lineEdit.text())+1))
    def remove(self):
        self.lineEdit.setText(str(int(self.lineEdit.text())-1))
    def encrypt(self):
        shift = int(self.lineEdit.text())
        text = self.textBrowser.toPlainText()
        ascii_from_text = [ord(c) for c in text]
        self.textBrowser_2.setText(''.join(chr(i+shift) for i in ascii_from_text))


if __name__ == '__main__':
    window = MainApp()
    sys.exit(window.exec())