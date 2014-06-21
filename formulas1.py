# -*- coding: utf-8 -*-
"""
Created on Fri Jun 20 21:06:34 2014

@author: chew-z
"""
import numpy as np
#import scipy.io as scio
import matplotlib.pyplot

def autocorr(x):
    result = np.correlate(x, x, mode='full')
    maxcorr = np.argmax(result)
    #print 'maximum = ', result[maxcorr]
    result = result / result[maxcorr]
    return result[result.size/2:]

def HPR(X, f):
# Holding Period Return - dla wektora X, danego f i największej straty min(X)
    return(1 + f * (- X / min(X)))
    
def TWR(X, f):
# Terminal Wealth Return z wektora X dla zadanego f
    return np.prod(HPR(X, f))

def f(X):
    f = 0.00
    k = 0.01
    while ( TWR(X, f) < TWR(X, f + k) ):
        if f > 1.0:
            break
        f = f + k
#if f -- 0 or f > 1 raise exception
    return(f)
    
def gvsf(X): # G vs. f (or GAT vs f or TWR vs f)
    n = len(X)
    # m = min(X)
    Y = []
    for i in xrange(100):
        fi = float(0.01*i)
        G = TWR(PL,fi) ** (1.0/n) - 1 # < 0 oznacza straty
        #GAT = G * (- m/fi);
        Y = Y + [[fi, G]]
    return(np.array(Y))

#d = scio.loadmat("PL.mat") #Matlab matrix with H1Close & DMA200
#PL = np.array(d['PL'][:,0]) #

#Using true random vector as P&L you can sometimes get incalculable results (exceptions etc.) try another
PL = 100*np.random.rand(10)-40 #skewed into profits a little for more practical demonstration

#1 Check P&L autocorrelation
matplotlib.pyplot.subplot(221)
matplotlib.pyplot.plot(autocorr(PL))
#2 Plot histogram P&L
matplotlib.pyplot.subplot(222)
matplotlib.pyplot.hist(PL)
#3 Plot cumulation of P&L
matplotlib.pyplot.subplot(223)
matplotlib.pyplot.plot(np.cumsum(PL))
#4 Plot G vs. f - if < 1 you are waisting time
X = gvsf(PL)
matplotlib.pyplot.subplot(224)
matplotlib.pyplot.plot(X[:,0], X[:,1]) 

matplotlib.pyplot.show()

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
