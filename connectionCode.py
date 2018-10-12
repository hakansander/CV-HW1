from PyQt5 import QtCore, QtGui, QtWidgets, uic
from PyQt5.QtWidgets import QFileDialog, QLabel
from PyQt5.QtGui import QPixmap
import sys


class MyWindow(QtWidgets.QMainWindow): 
    def __init__(self):
        super(MyWindow, self).__init__()
        uic.loadUi('userInterface.ui', self) #loads the uid from the file and parse it into the code
        #OPENİNG IMAGE!
        self.actionOpen_Target.triggered.connect(self.openImage)

        def PrintSomething(self):
            print("Hello world")

    #Image opening function!!!!
    def openImage(self):
        imagePath, _ = QFileDialog.getOpenFileName()
        pixmap = QPixmap(imagePath)
        self.label.setPixmap(pixmap)

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())
