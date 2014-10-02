# -*- coding: utf-8 -*-
"""
Created on Wed Oct  1 16:00:26 2014
1) Plot candlestick from MQL data (with data window b:e)
@author: chew-z
"""
import read_mql as read_mql
import matplotlib.pyplot as plt
from matplotlib.finance import candlestick2

# 1 import OHLC
csv_listD1 = read_mql.csv_to_list('./data/EURUSD1440_01.csv')

d_mat = read_mql.convert_cells_to_floats(csv_listD1, 1, 3)
openD1 = d_mat[:, 0]
highD1 = d_mat[:, 1]
lowD1 = d_mat[:, 2]
closeD1 = d_mat[:, 3]

del d_mat, csv_listD1

b = 1070
e = 1090
#2 plot candlesticks
fig, ax = plt.subplots()
plt.setp(ax, xlim=[b, e], ylim=[min(lowD1[b:e]), max(highD1[b:e])])
candlestick2(ax, openD1, closeD1, 
             highD1, lowD1, 0.5, 'g', 'r')
   
del b, e