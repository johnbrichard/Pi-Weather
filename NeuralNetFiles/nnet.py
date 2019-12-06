#from __future__ import absolute_import, division, print_function, unicode_literals

# TensorFlow and tf.keras
#import tensorflow as tf
#from tensorflow import keras

# Helper libraries
#import numpy as np
#import matplotlib.pyplot as plt

def dataImport(tFile,hFile, temp, hum, tempWeight, humWeight):
    tempFile=open(tFile,"r")
    humFile=open(hFile, "r")

    temp = [int(x.strip()) for x in tempFile.readlines()]
    hum = [int(x.strip()) for x in humFile.readlines()]
    tempWeight=[(x/75) for x in temp]
    humWeight=[(x/40) for x in hum]
    print(round(temp[2000],2),round(tempWeight[2000],2),round(hum[2000],2),round(humWeight[2000]))

def main():
    temperatures=[]
    humidities=[]
    temperatureWeights=[]
    humidityWeights=[]

    dataImport('temps.txt','hums.txt',temperatures,humidities,temperatureWeights,humidityWeights)
    print()

if __name__ == '__main__':
    main()