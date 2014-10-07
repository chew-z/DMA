# -*- coding: utf-8 -*-
"""
Created on Wed Oct  1 16:00:26 2014
1) Plot candlestick from MQL data (with data window b:e)
@author: chew-z
"""
import matplotlib.pyplot as plt
from matplotlib.finance import candlestick2

# 1 read OHLC
g = globals()  # read global variables
d_mat = g['d_mat']
returns = g['returns']

openD1 = d_mat[:, 0]
highD1 = d_mat[:, 1]
lowD1 = d_mat[:, 2]
closeD1 = d_mat[:, 3]

b = 4095
e = 4105
#2 plot candlesticks
fig, ax = plt.subplots()
plt.setp(ax, xlim=[b, e], ylim=[min(lowD1[b:e]), max(highD1[b:e])])
candlestick2(ax, openD1, closeD1, 
             highD1, lowD1, 0.5, 'g', 'r')
   
del b, e, openD1, highD1, lowD1, closeD1