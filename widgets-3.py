#TEST FILE USING CLASS

import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget

class Window(QMainWindow):

    def __init__(self):
        super(Window,self).__init__()
        self.initUI()


    def button(self):
        self.lab1.setText('You clicked me')

    def initUI(self):

        self.setGeometry(200,200,200,200)
        self.setWindowTitle('HEY')
        self.lab1 = QtWidgets.QLabel(self)
        self.lab1.setText(' label ')
        self.lab1.move(20,20)
        self.but1 = QtWidgets.QPushButton(self)
        self.but1.setText('button')
        self.but1.move(50,50)
        self.but1.clicked.connect(self.button)



    def update(self):
        self.lab1.adjustSize()

def window():
    app = QApplication(sys.argv)
    win = Window()
    win.show()
    sys.exit(app.exec_())


window()
