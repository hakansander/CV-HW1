#Student Name:   Hakan Sander
#Student Number: 150140146
#Date:

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
    plt.show()
