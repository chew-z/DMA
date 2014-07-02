# -*- coding: utf-8 -*-
"""
1) Testing TA-Lib and it's cpython wraper

Created on Fri Jun 27 23:09:39 2014
@author: chew-z
"""
import numpy as np
import scipy.io as scio
import matplotlib.pyplot
import talib

d_mat = scio.loadmat("Close.mat") #Matlab matrix with Close
close = np.array(d_mat['C'][:, 0])

sma = talib.SMA(close)
mx = talib.MAX(close, 1000)
mn = talib.MIN(close, 1000)

# Plot close i sma
matplotlib.pyplot.plot(close)
matplotlib.pyplot.plot(sma)
matplotlib.pyplot.plot(mx)
matplotlib.pyplot.plot(mn)
matplotlib.pyplot.show()
