#WITHOUT CLASS(LABELS AND BUTTONS)
 import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5 import QtWidgets

def but1f():
    print('hey im but1')
def but2f():
    print('hey im but2')
def but3f():
    print('hey im but3')
def main():
    app = QApplication(sys.argv)
    w = QWidget()
    w.setWindowTitle('Practise')
    w.setGeometry(500,500,500,500)
    lab1 = QtWidgets.QLabel(w)
    lab1.setText('lab1')
    lab1.move(50,50)
    lab2 = QtWidgets.QLabel(w)
    lab2.setText('lab2')
    lab2.move(100,100)
    lab3 = QtWidgets.QLabel(w)
    lab3.setText('lab3')
    lab3.move(150,150)
    but1 = QtWidgets.QPushButton(w)
    but1.setText('but1')
    but1.clicked.connect(but1f)
    but1.move(50,120)
    but2 = QtWidgets.QPushButton(w)
    but2.clicked.connect(but2f)
    but2.setText('but2')
    but2.move(100,210)
    but3 = QtWidgets.QPushButton(w)
    but3.clicked.connect(but3f)
    but3.setText('but3')
    but3.move(150,270)

    w.show()
    sys.exit(app.exec_())

main()
