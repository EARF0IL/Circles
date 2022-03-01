import sys

from PyQt5 import uic
from random import randint
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QPainter, QColor


class Application(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)
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
                painter.setBrush(QColor(255, 255, 0))
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
