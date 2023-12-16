import os
import ctypes
import platform
import logging

from PyQt5 import QtCore, QtWidgets
from ui_mainwindow import Ui_Form


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.ui = Ui_Form()
        self.ui.setupUi(self)
        QtWidgets.QGraphicsView()

    def 


if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    application = MainWindow()
    application.show()
    app.exec()