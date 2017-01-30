import numpy as np
##from (library) import (specific library function)
import pandas as pd
#from pandas import DataFrame, read_csv 
import urllib
import time
#import requests
import csv
#from textblob import TextBlob

import ProcessData as proD
label_data = proD.readFileandConverttoNumpy('Feature_values.csv')
label_values = proD.readFileandConverttoNumpy('Label_values.csv')
dataFrame = proD.readFileandConverttoNumpy('EnglishMoviesWithBo.csv')

features_train = label_data[0:2300]
labels_train = label_values[0:2300]
features_test = label_data[2300:]
labels_test = label_values[2300:]


predictions = proD.SVMLearning(features_train,labels_train,features_test)
#print features_train.shape
#print labels_train.shape

target = open("Results.txt", 'w')


for i in range(0,len(predictions)):
        target.write( dataFrame[2301+i][9])
        target.write("\n")
        collection = labels_test[i].astype(float)
        target.write("Actual value is ")
        target.write(collection.astype(str) )
        target.write("\n")
        target.write("predicted value :")
        target.write(predictions[i].astype(str))
        target.write("\n")
        target.write( "Error percentage is ")
        error = ((collection -predictions[i])/collection )*100
        #print error
        target.write(error.astype(str))
        target.write("\n")
        target.write("-----------------------------")
        target.write("\n")
target.close()
#print  dataFrame[0][9]
