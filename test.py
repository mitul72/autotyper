from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication,QMainWindow
import sys

def window():
    app=QApplication(sys.argv)
    win=QMainWindow()
#   win.setGeometry(xpos,ypos,width,height)
    win.setGeometry(200,200,700,300)
    win.setWindowTitle("mitul's application")

    label=QtWidgets.QLabel(win)
    label.setText("Hello World!")
    label.move(50,50)

    win.show()
    sys.exit(app.exec_())

window()

#test
