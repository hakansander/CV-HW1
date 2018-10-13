#Student Name:   Hakan Sander
#Student Number: 150140146
#Date: 12.10.2018

#This file contains the printing operation codes of all the histograms
#Although there is no need to print the histograms of PDF and CDF,
#I have plotted them to check the correctness of the code and observe the results of PDF and CDF

import numpy as np
import matplotlib.pyplot as plt

#colorIntensities: (3,256) numpy array that contains intensity frequencies of B,G,R channels respectively
#intensityRange: (256) 1D numpy array that is given for the creation of the intensity range,
#                 this variable represents the ending of the range i.e. (0......255), that is 255 for this vector
def printHistogram(colorIntensities, intensityRange, histogramName):
    intensityRange = np.linspace(start=0,stop=intensityRange,num=256)

    plt.figure(figsize=(5,5))
    plt.subplot(311)
    plt.bar(intensityRange, colorIntensities[2], color="red")
    plt.subplot(312)
    plt.bar(intensityRange, colorIntensities[1], color="green")
    plt.subplot(313)
    plt.bar(intensityRange, colorIntensities[0], color="blue")
    plt.savefig(histogramName + ".png")

#histogramCDF: Calculated CDF of the given image
#windowTitle: The title which pops up on the top left of the matplotlib window
#operationName: The desired operation name that is opened below the CDF
def printHistogramCDF(histogramCDF, windowTitle, operationName):
    #using the 2 lines code below, window's title is changed
    fig = plt.figure()
    fig.canvas.set_window_title(windowTitle)

    ax1 = plt.subplot(2,2,1)
    ax1.set_title('Blue channel {}histogram of img'.format(operationName))
    plt.plot(histogramCDF[0], 'b')

    ax2 = plt.subplot(2,2,2)
    ax2.set_title('Green channel {}histogram of img'.format(operationName))
    plt.plot(histogramCDF[1], 'g')

    ax3 = plt.subplot(2,2,3)
    ax3.set_title('Red channel {}histogram of img'.format(operationName))
    plt.plot(histogramCDF[2], 'r')

    ax4 = plt.subplot(2,2,4)
    plt.plot(histogramCDF[0], 'b', label="blue channel")
    plt.plot(histogramCDF[1], 'g', label="green channel")
    plt.plot(histogramCDF[2], 'r', label="red channel")
    plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left', borderaxespad=0.)
    ax4.set_title('{} Histogram of all channels of img'.format(operationName))
    plt.show()
