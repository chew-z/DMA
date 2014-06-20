# -*- coding: utf-8 -*-
"""
Created on Fri Jun 20 21:06:34 2014

@author: chew-z
"""
import numpy as np
import scipy.io as scio

def HPR(X, f):
# Holding Period Return - dla wektora X, danego f i największej straty min(X)
    return(1 + f * (- X / min(X)))
    
def TWR(X, f):
# Terminal Wealth Return z wektora X dla zadanego f
    return np.prod(HPR(X, f))

def f(X):
    f = 0.01
    k = 0.01
    while ( TWR(X, f) < TWR(X, f + k) ):
        if f > 1.0:
            break
        f = f + k
    return(f)

#d = scio.loadmat("PL.mat") #Matlab matrix with H1Close & DMA200
#PL = np.array(d['PL'][:,0]) #
PL = 100*np.random.rand(10)-40

f = f(PL)

largest_loss = min(PL)
print "Optimum f: ", f
f_dollar = -largest_loss/f
print "f dollar: ", f_dollar
twr = TWR(PL, f)
print "Terminal Wealth Return = ", twr
g = twr ** (1.0/len(PL)) - 1
print "G = ", g
gat = g * (- largest_loss/f)
print "Geometric Average Trade = ", gat
