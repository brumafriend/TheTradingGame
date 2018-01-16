import sys
from PyQt5.QtWidgets import QApplication, QWidget
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
        button.setToolTip('This is an example button')
        button.move(100,70) 
        button.clicked.connect(self.on_click)

        savebut = QPushButton(QIcon('save.png'),'Save', self)
        savebut.setToolTip('This is an example button')
        savebut.move(400,70) 
        savebut.clicked.connect(self.on_click)

        progressbut = QPushButton(QIcon('progress.png'),'Progress', self)
        progressbut.setToolTip('This is an example button')
        progressbut.move(700,70) 
        progressbut.clicked.connect(self.on_click)

        assetsbut = QPushButton(QIcon('assets.png'),'My Assets', self)
        assetsbut.setToolTip('This is an example button')
        assetsbut.move(90,370) 
        assetsbut.clicked.connect(self.on_click)

        but = QPushButton(QIcon('progress.png'),'Progress', self)
        but.setToolTip('This is an example button')
        but.move(390,370) 
        but.clicked.connect(self.on_click)

        but = QPushButton(QIcon('progress.png'),'Progress', self)
        but.setToolTip('This is an example button')
        but.move(690,370) 
        but.clicked.connect(self.on_click)

        self.show()
    @pyqtSlot()       
    def on_click(self):
        print('Investing')
 
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
