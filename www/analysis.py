#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'Hehao'

import pandas as pd
import matplotlib.pyplot as plt

def showPlot():
    mtl=pd.read_csv('cryptocurrency.csv',header=0,sep=';',index_col='Date')
    mtl.head(3)
    mtl.index=pd.to_datetime(mtl.index)
    #close price
    Close=mtl.Close
    # plt.plot(Close)
    plt.hist(Close)
    
def openDataFile(filePath):
     data=pd.read_csv(filePath,header=0,sep=';',index_col='Date')
     return data
 
def getVar(data):
     return data.var()
 
def getStd(data):
     return data.std()
 
 
    
if __name__ == '__main__':
    #showPlot()
  data=  openDataFile('cryptocurrency.csv')
  print('var:%s'% getVar(data)) 
  