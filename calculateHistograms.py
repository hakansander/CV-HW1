#Student Name:   Hakan Sander
#Student Number: 150140146
#Date:

import cv2
import numpy as np

def computeImageHistogram(img):
    totalRows = img.shape[0]
    totalColumns = img.shape[1]
    totalPixels = totalRows * totalColumns

    colorIntensities = np.zeros((img.shape[2], 256))    #color intensities contains 0,1,2...255 intensity values

    for channel in range(img.shape[2]):
        for i in range(totalRows):
            for j in range(totalColumns):
                colorIntensities[channel][img[i][j][channel]] += 1
    return colorIntensities

def calculatePDF(colorIntensities):
    totalChannels = colorIntensities.shape[0]                #total number of channels is 3 which are Blue, Green and Red channels
    intensityRange = colorIntensities.shape[1]               #intensity range is 256 for this question
    histogramPDF = np.zeros((totalChannels, intensityRange)) #create a (3,256) matrix in order to store the calculated histogram PDF
    for i in range(totalChannels):
        histogramPDF[i,:] = colorIntensities[i,:] / sum(colorIntensities[i,:]) #divide each channel to total number of pixels in order to obtain PDF
    return histogramPDF

def calculateCDF(histogramPDF):
    histogramCDF = np.zeros((histogramPDF.shape[0], histogramPDF.shape[1]))
    for i in range(histogramPDF.shape[0]): #loop through blue, green, red channels
        histogramCDF[i] = np.cumsum(histogramPDF[i]) #calculate CDF using each of their PDF
    return histogramCDF

if __name__ == '__main__':
    inputImage = cv2.imread("color1.png", 1)
    colorIntensities = computeImageHistogram(inputImage)
    histogramPDF = calculatePDF(colorIntensities)
    histogramCDF = calculateCDF(histogramPDF)
