import sys

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5 import uic
from random import randint
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QPainter, QColor


class Ui_mainWindow(object):
    def setupUi(self, mainWindow):
        mainWindow.setObjectName("mainWindow")
        mainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(mainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(190, 560, 381, 31))
        self.pushButton.setObjectName("pushButton")
        mainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(mainWindow)
        QtCore.QMetaObject.connectSlotsByName(mainWindow)

    def retranslateUi(self, mainWindow):
        _translate = QtCore.QCoreApplication.translate
        mainWindow.setWindowTitle(_translate("mainWindow", "Circles"))
        self.pushButton.setText(_translate("mainWindow", "Button"))


class Application(QMainWindow, Ui_mainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.can_paint = False
        self.pushButton.clicked.connect(self.but_click)

    def but_click(self):
        self.can_paint = True
        self.update()

    def paintEvent(self, event):
        if self.can_paint:
            for i in range(randint(1, 100)):
                painter = QPainter()
                painter.begin(self)
                painter.setBrush(QColor(randint(0, 255), randint(0, 255), randint(0, 255)))
                r = randint(1, 100)
                painter.drawEllipse(randint(0, self.width()), randint(0, self.height()), r, r)
                painter.end()
                self.can_paint = False


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = Application()
    ex.show()
    sys.excepthook = except_hook
    sys.exit(app.exec())
