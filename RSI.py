# -*- coding: utf-8 -*-
"""
Created on Tue Feb 28 22:23:28 2017

@author: cranial
"""
import numpy as np
from numpy import genfromtxt
m=0
dataset = genfromtxt('table.csv',delimiter=',')
ClosingP = dataset[1:,4,None]
"""Relative Strength Index"""
m=0
M=0
def CalcAvgs(x):
    change = np.zeros((x.shape[0],1))
    gain = np.zeros((0,0))
    loss = np.zeros((0,0))
    for i in range(x.shape[0]):
        if i <x.shape[0]-1:        
            change[i,0] = x[i,0] - x[i+1,0];
        if change[i,0] >= 0:
            gain =np.append(gain,change[i,0])
            gain = gain.reshape((gain.shape[0],1))
        else:
            loss =np.append(loss,change[i,0])
            loss = loss.reshape((loss.shape[0],1))
    return gain,loss
def CalcRSI(x,period=14):
    RSI = np.zeros((0,0))
    for i in range(x.shape[0]):
        if i <1844:            
            param = x[i:i+period,0,None]
            g,l = CalcAvgs(param)
            avgG = np.average(g)
            avgL = np.average(l)
            RS = avgG/avgL
            mid = 100 - (100/RS)
            RSI = np.append(RSI,mid)
            RSI = np.reshape(RSI,(RSI.shape[0],1))
    return RSI
            
"""    
seed = np.random.random(100);
seed = np.reshape(seed,(100,1))
g,l = CalcAvgs(seed)
print g,l
"""
rsi = CalcRSI(ClosingP)
print rsi.shape


