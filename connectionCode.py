#Student Name:   Hakan Sander
#Student Number: 150140146
#Date: 12.10.2018

from __future__ import unicode_literals
from PyQt5 import QtCore, QtGui, QtWidgets, uic
from PyQt5.QtWidgets import QFileDialog, QLabel
from PyQt5.QtGui import QPixmap
import sys, os, matplotlib, cv2
import numpy as np

import matplotlib.pyplot as plt

import calculateHistograms as histCalc
import printHistograms as printHist

class MyWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        uic.loadUi('userInterface.ui', self) #loads the uid from the file and parse it into the code

        self.imagePath = '' #image path is held in this variable when the images are opened

        self.inputImage = []
        self.targetImage = []

        self.inputImageFlag = False  #this variable is assigned to True when the input image is loaded
        self.targetImageFlag = False #this variable is assigned to True when the target image is loaded

        self.colorIntensitiesInput = []  #in this variable input image intensity frequencies for each channel is saved
        self.colorIntensitiesTarget = [] #in this variable target image intensity frequencies for each channel is saved

        self.actionOpen_Input.triggered.connect(self.openInputImage)    #open input image when the open input in the menu is clicked
        self.actionOpen_Target.triggered.connect(self.openTargetImage)  #open target image #open input image when the open target in the menu is clicked
        self.actionExit.triggered.connect(self.exitProgram)             #exit the program when the exit is clicked on the menu

        self.equalizeButton.clicked.connect(self.match) #when the equalize button is clicked, call match function

    def match(self):
        #if both images are loaded, then apply histogram matching
        if(self.inputImageFlag == True and self.targetImageFlag == True):

            histogramPDF_Input = histCalc.calculatePDF(self.colorIntensitiesInput)
            histogramCDF_Input = histCalc.calculateCDF(histogramPDF_Input)

            histogramPDF_Target = histCalc.calculatePDF(self.colorIntensitiesTarget)
            histogramCDF_Target = histCalc.calculateCDF(histogramPDF_Target)

            #for each of the B,G,R channels create a LUT and save it to LUT numpy array
            LUT = np.zeros((3,256))
            for i in range(3):
                LUT[i,:] = histCalc.createLUT(self.inputImage, self.targetImage, histogramCDF_Input[i], histogramCDF_Target[i])

            self.copiedInputImage = np.copy(self.inputImage) #since the inputImage is modified inside the hisotgramMatching, we should copy it. Otherwise, multiple clicks of the equalizeButton gives erroneous results

            matchedInputImg = histCalc.HistogramMatching(LUT, self.copiedInputImage)

            cv2.imwrite("matchedInputImage.png", matchedInputImg)

            pixmap = QPixmap("matchedInputImage.png")
            self.label_3.setPixmap(pixmap)

            colorIntensitiesMatchedImg = histCalc.computeImageHistogram(matchedInputImg)
            newMatchedInputImg = np.zeros((matchedInputImg.shape[2], matchedInputImg.shape[0], matchedInputImg.shape[1]))
            newMatchedInputImg[0] = matchedInputImg[:,:,0]
            newMatchedInputImg[1] = matchedInputImg[:,:,1]
            newMatchedInputImg[2] = matchedInputImg[:,:,2]

            outputImgHistName = "outputImageHistogram"
            printHist.printHistogram(colorIntensitiesMatchedImg, 255, outputImgHistName)

            pixmap = QPixmap(outputImgHistName + ".png")
            self.outputImageHistogram.setPixmap(pixmap)

        #elif the inputImage is not loaded, show an error message
        elif not self.inputImageFlag:
            print("You have not selected an input image yet!")

        #elif the targetImage is not loaded, show an error message
        elif not self.targetImageFlag: #elif the targetImage
            print("You have not selected a target image yet!")

    #Image opening function used for target image
    def openInputImage(self):
        self.imagePath, _ = QFileDialog.getOpenFileName() #get the file path
        self.inputImageFlag = True

        #draw image to label that is created in the ui by importing from the indicated imagePath
        pixmap = QPixmap(self.imagePath)
        self.label.setPixmap(pixmap)

        self.inputImage = cv2.imread(self.imagePath, 1)

        intensityRange = np.linspace(start=0,stop=255,num=256)

        self.colorIntensitiesInput = histCalc.computeImageHistogram(self.inputImage)

        inputImgHistName = "inputImageHistogram"
        printHist.printHistogram(self.colorIntensitiesInput, 255, inputImgHistName)

        pixmap = QPixmap(inputImgHistName + ".png")
        self.inputImageHistogram.setPixmap(pixmap)

    #Image opening function used for target image
    def openTargetImage(self):
        self.imagePath, _ = QFileDialog.getOpenFileName()
        self.targetImageFlag = True
        pixmap = QPixmap(self.imagePath)
        self.label_2.setPixmap(pixmap)

        self.targetImage = cv2.imread(self.imagePath, 1)

        intensityRange = np.linspace(start=0,stop=255,num=256)

        self.colorIntensitiesTarget = histCalc.computeImageHistogram(self.targetImage)

        targetImgHistName = "targetImageHistogram"
        printHist.printHistogram(self.colorIntensitiesTarget, 255, targetImgHistName)

        pixmap = QPixmap(targetImgHistName + ".png")
        self.targetImageHistogram.setPixmap(pixmap)

    #when the exit button on the menu is clicked, call the function below and exit the program
    def exitProgram(self):
        app.quit()

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = MyWindow()
    window.setWindowTitle("Histogram Equalization")
    window.showMaximized()
    sys.exit(app.exec_())
