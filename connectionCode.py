from __future__ import unicode_literals
from PyQt5 import QtCore, QtGui, QtWidgets, uic
from PyQt5.QtWidgets import QFileDialog, QLabel
from PyQt5.QtGui import QPixmap

import sys
import os
import random
import matplotlib
# Make sure that we are using QT5
matplotlib.use('Qt5Agg')

from numpy import arange, sin, pi
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure



class MyWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        uic.loadUi('userInterface.ui', self) #loads the uid from the file and parse it into the code
        #OPENİNG IMAGE!
        self.actionOpen_Target.triggered.connect(self.openImage)

        sc = MyStaticMplCanvas(self.widget, width=2, height=2, dpi=100)
        dc = MyDynamicMplCanvas(self.widget, width=2, height=2, dpi=100)

    #Image opening function used for target image
    def openImage(self):
        imagePath, _ = QFileDialog.getOpenFileName()
        pixmap = QPixmap(imagePath)
        self.label.setPixmap(pixmap)


class MyMplCanvas(FigureCanvas):
    """Ultimately, this is a QWidget (as well as a FigureCanvasAgg, etc.)."""

    def __init__(self, parent=None, width=5, height=4, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)

        self.compute_initial_figure()

        FigureCanvas.__init__(self, fig)
        self.setParent(parent)

        FigureCanvas.setSizePolicy(self,
                                   QtWidgets.QSizePolicy.Expanding,
                                   QtWidgets.QSizePolicy.Expanding)
        FigureCanvas.updateGeometry(self)

    def compute_initial_figure(self):
        pass


class MyStaticMplCanvas(MyMplCanvas):
    """Simple canvas with a sine plot."""

    def compute_initial_figure(self):
        t = arange(0.0, 3.0, 0.01)
        s = sin(2*pi*t)
        self.axes.plot(t, s)


class MyDynamicMplCanvas(MyMplCanvas):
    """A canvas that updates itself every second with a new plot."""

    def __init__(self, *args, **kwargs):
        MyMplCanvas.__init__(self, *args, **kwargs)
        timer = QtCore.QTimer(self)
        timer.timeout.connect(self.update_figure)
        timer.start(1000)

    def compute_initial_figure(self):
        self.axes.plot([0, 1, 2, 3], [1, 2, 0, 4], 'r')

    def update_figure(self):
        # Build a list of 4 random integers between 0 and 10 (both inclusive)
        l = [random.randint(0, 10) for i in range(4)]
        self.axes.cla()
        self.axes.plot([0, 1, 2, 3], l, 'r')
        self.draw()


if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = MyWindow()
    window.showMaximized()
    sys.exit(app.exec_())
