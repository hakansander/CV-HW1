#Student Name:   Hakan Sander
#Student Number: 150140146
#Date: 12.10.2018

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

#creates LUT for the histogram matching using CDF of input image and target image
def createLUT(inputImg, targetImg, CDF_InputImg, CDF_TargetImg):
    LUT = np.zeros(256)
    g_j = 0
    for g_i in range(256):
        while(CDF_InputImg[g_i] > CDF_TargetImg[g_j] and g_j < 255):
            g_j += 1
        LUT[g_i] = g_j
    return LUT

#assigns to an intensity on the LUT for each pixel intensity in the inputImg
def HistogramMatching(LUT, inputImg):
    totalRows, totalColumns, totalChannels = inputImg.shape
    for ch in range(totalChannels):
        for i in range(totalRows):
            for j in range(totalColumns):
                inputImg[i,j,ch] = LUT[ch, inputImg[i, j, ch]]

    return inputImg
