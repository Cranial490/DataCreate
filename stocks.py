from numpy import genfromtxt
import numpy as np

#Stochastic K%

dataset = genfromtxt('table.csv',delimiter=',')
ClosingP = dataset[1:,4,None]
def CalcK(x):
    m=np.amin(x)
    M=np.amax(x)
    K = (x[0,0] - m)/float((M-m))
    return K*100
#------------------------------------------------------------------------------
mini = np.zeros((10,1))
K = np.zeros((1844,1))
print K.shape
for i in range(ClosingP.shape[0]):
    while i<1844:
        mini = ClosingP[i:i+10,0,None]
        K[i,0] = CalcK(mini)
        break
    
# Stochastic D%
D = np.zeros(K.shape) 
s=0
for i in range(D.shape[0]):
    for j in range(3):
        if i<1842:
            s = s + K[j+i,0]
    D[i,0] = s/3
    s=0
"""Matter ho gya hai manually K% calculate karke value dalna padega"""
for k in range(1842,1844):
    D[k,0]=K[k,0]
