import sys

from PyQt5 import QtGui
from PyQt5.QtWidgets import QWidget, QPushButton, QApplication, QDesktopWidget
from PyQt5.QtCore import QCoreApplication
import qtetris
class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        #self.qtetris = qtetris.QTetris(primary_win = self)
    def initUI(self):
        qbtn = QPushButton('Exit', self)
        qbtn.clicked.connect(QCoreApplication.instance().quit)
        qbtn.resize(qbtn.sizeHint())

        pall = self.palette()
        pall.setBrush(QtGui.QPalette.Normal, QtGui.QPalette.Window, QtGui.QBrush(QtGui.QPixmap("10.jpg")))
        self.setPalette(pall)

        qbtn.move(290, 370)
        self.qbtn2 = QPushButton('Start Game', self)
        self.qbtn2.clicked.connect(self.showQTetris)
        self.qbtn2.resize(qbtn.sizeHint())
        self.qbtn2.move(170, 370)
        self.setGeometry(20, 20, 620, 540)
        self.setWindowTitle('Obolochka')
        self.qtetris = qtetris.QTetris(primary_win=self)
        self.center()
        self.show()

    def center(self):
        screen = QDesktopWidget().screenGeometry()
        size = self.geometry()
        self.move((screen.width() - size.width()) / 2, (screen.height() - size.height()) / 2)
    def showQTetris(self):
        if not self.qtetris:
            self.qtetris = qtetris.QTetris(primary_win = self)
        self.qtetris.show()
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())