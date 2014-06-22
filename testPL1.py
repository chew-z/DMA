# -*- coding: utf-8 -*-
"""
Torturing Profit & Loss (PL) of a trading system
Created on Fri Jun 20 21:06:34 2014

@author: chew-z
"""
import numpy as np
#import scipy.io as scio
import matplotlib.pyplot

import formulas as formulas

#d = scio.loadmat("PL.mat") #Matlab matrix with H1Close & DMA200
#PL = np.array(d['PL'][:,0]) #

#Using true random vector as P&L you can sometimes get incalculable results (exceptions etc.) try another
PL = 100*np.random.rand(10)-40 #skewed into profits a little for more practical demonstration

#1 Check P&L autocorrelation
matplotlib.pyplot.subplot(221)
matplotlib.pyplot.plot(formulas.autocorr(PL))
#2 Plot histogram P&L
matplotlib.pyplot.subplot(222)
matplotlib.pyplot.hist(PL)
#3 Plot cumulation of P&L
matplotlib.pyplot.subplot(223)
matplotlib.pyplot.plot(np.cumsum(PL))
#4 Plot G vs. f - if < 1 you are waisting time
X = formulas.gvsf(PL)
matplotlib.pyplot.subplot(224)
matplotlib.pyplot.plot(X[:,0], X[:,1]) 

matplotlib.pyplot.show()

f = formulas.f(PL)

largest_loss = min(PL)
print "Optimum f: ", f
f_dollar = -largest_loss/f
print "f dollar: ", f_dollar
twr = formulas.TWR(PL, f)
print "Terminal Wealth Return = ", twr
g = twr ** (1.0/len(PL)) - 1
print "G = ", g
gat = g * (- largest_loss/f)
print "Geometric Average Trade = ", gat
