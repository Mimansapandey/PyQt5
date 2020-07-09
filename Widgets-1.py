import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton, QToolTip)
from PyQt5.QtGui import QIcon, QFont

class PyQt(QWidget):

  def main():

    app = QApplication(sys.argv)
    #creating a widget
    w = QWidget()
    #resize changes the height and width of the box
    w.resize(500, 500)
    #the widget will be on screen at x=300, y=300
    w.move(300, 300)
    #setting the window title
    w.setWindowTitle('PyQt')
    #locates the box on screen and sets its size
    w.setGeometry(300, 300, 300, 220)
    w.setWindowIcon(QIcon('web.png'))
    #deciding the font and its size
    QToolTip.setFont(QFont('SansSerif', 10))
    #we call the setToolTip() method
    w.setToolTip('This is a button')
    #We create a push button widget and set a tooltip for it
    btn = QPushButton('Button',w)
    #setting a tooltip for it
    btn.setToolTip('This is a button')
    #The button is being resized and moved on the window.
    # The sizeHint() method gives a recommended size for the button.
    btn.resize(btn.sizeHint())
    btn.move(50, 50)

    w.setGeometry(300, 300, 300, 200)
    #on clicking this button the application terminates
    #first parameter is the label of the button and the second parameter is the parameter widget
    Qbut = QPushButton('Quit', w)
    #this processes and dispatches all events and then the clicked signal is connected to the quit() meathod
    #which terminates the application
    Qbut.clicked.connect(QApplication.instance().quit)
    #gives the recommended size for the button
    Qbut.resize(Qbut.sizeHint())
    Qbut.move(150, 50)
    w.show()

    sys.exit(app.exec_())

  if __name__ == '__main__':
    main()
