import sys
import tkinter
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.QtCore import pyqtSlot
 
class App(QWidget):
 
    def __init__(self):
        super().__init__()
        self.title = 'The Trading Game'
        self.left = 10
        self.top = 10
        self.width = 900
        self.height = 600
        self.initUI()
 
    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        
        button = QPushButton(QIcon('invest.png'),'Invest', self)
        button.move(100,70) 
        button.clicked.connect(self.investwin)

        savebut = QPushButton(QIcon('save.png'),'Save', self)
        savebut.move(400,70) 
        savebut.clicked.connect(self.investwin)

        progressbut = QPushButton(QIcon('progress.png'),'Progress', self)
        progressbut.move(700,70) 
        progressbut.clicked.connect(self.investwin)

        assetsbut = QPushButton(QIcon('assets.png'),'My Assets', self)
        assetsbut.move(90,370) 
        assetsbut.clicked.connect(self.investwin)

        but = QPushButton(QIcon('progress.png'),'Progress', self)
        but.move(390,370) 
        but.clicked.connect(self.investwin)

        but = QPushButton(QIcon('progress.png'),'Progress', self)
        but.move(690,370) 
        but.clicked.connect(self.investwin)

        self.show()
    @pyqtSlot()       
    def investwin(self):
        root = Tk()
        root.geometry('900x600')
        root.title('Invest')
 
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
 
 
