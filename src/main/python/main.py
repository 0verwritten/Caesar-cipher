from fbs_runtime.application_context.PyQt5 import ApplicationContext
from PyQt5 import QtWidgets,QtCore,QtGui

from design import Ui_MainWindow
import sys


class MainApp(QtWidgets.QApplication, Ui_MainWindow):
    def __init__(self):
        super(MainApp, self).__init__([])
        self.mainwindow = QtWidgets.QMainWindow()
        self.setupUi(self.mainwindow)
        self.lineEdit.setValidator(QtGui.QIntValidator())
        self.pushButton_2.pressed.connect(self.add)
        self.pushButton.pressed.connect(self.remove)
        self.lineEdit.textChanged.connect(self.shift_changed)
        self.lineEdit.textChanged.connect(self.encrypt)
        self.textBrowser.textChanged.connect(self.encrypt)
        self.textBrowser_2.textChanged.connect(self.decrypt)
        self.shift=0
        self.entext = ""
        self.detext = ""
        self.lastfocus = ''
        self.mainwindow.show()
    def add(self):
        self.lineEdit.setText(str(int(self.lineEdit.text())+1))
        self.encrypt()
        self.decrypt()
    def remove(self):
        self.lineEdit.setText(str(int(self.lineEdit.text())-1))
        self.encrypt()
        self.decrypt()
    def encrypt(self):
        if not self.textBrowser_2.hasFocus():
            shift = self.shift
            self.entext = self.textBrowser.toPlainText()
            text = self.entext
            ascii_from_text = [ord(c) for c in text]
            try:
                self.textBrowser_2.setText(''.join(chr(i+shift) for i in ascii_from_text))
            except ValueError:
                try:
                    self.textBrowser.setText(''.join(chr(1114112+i+shift) for i in ascii_from_text))
                except Exception as e:
                    pass
    def decrypt(self):
        if self.textBrowser_2.hasFocus():
            shift = -self.shift
            self.detext = self.textBrowser_2.toPlainText()
            text = self.detext
            ascii_from_text = [ord(c) for c in text]
            try:
                self.textBrowser.setText(''.join(chr(i+shift) for i in ascii_from_text))
            except ValueError:
                try:
                    self.textBrowser.setText(''.join(chr(1114112+i+shift) for i in ascii_from_text))
                except Exception as e:
                    pass
    def shift_changed(self):
        try:
            self.shift = int(self.lineEdit.text())
        except ValueError:
            pass

if __name__ == '__main__':
    window = MainApp()
    sys.exit(window.exec())