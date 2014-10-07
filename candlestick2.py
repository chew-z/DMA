# -*- coding: utf-8 -*-
"""
Created on Wed Oct  1 16:00:26 2014
1) Plot candlestick from MQL data (with data window b:e)
@author: chew-z
"""
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.finance import candlestick2

# 1 read OHLC
g = globals()  # read global variables
d_mat = g['d_mat']
returns = g['returns']

openD1 = d_mat[:, 0]
highD1 = d_mat[:, 1]
lowD1 = d_mat[:, 2]
closeD1 = d_mat[:, 3]

# take largest wins
index_sorted = np.argsort(returns)[-5:-1]
#2 plot candlesticks
fig, subplt = plt.subplots(4, 1)

i = 0
for ax in subplt:
    #plt.setp(ax, xlim=[b, e], ylim=[min(lowD1[b:e]), max(highD1[b:e])])
    b = index_sorted[i]-5
    e = index_sorted[i]+5
    candlestick2(ax, openD1[b:e], closeD1[b:e], 
             highD1[b:e], lowD1[b:e], 0.5, 'g', 'r')
    i += 1
   
del b, e, openD1, highD1, lowD1, closeD1, index_sorted