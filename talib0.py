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
import read_mql as mql

#d_mat = mql.convert_cells_to_floats(mql.csv_to_list('./data/EURUSD60_01.csv'), 1, 3)
close = np.random.sample([1000])
#del d_mat

sma = talib.SMA(close)
mx = talib.MAX(close, 1000)
mn = talib.MIN(close, 1000)

# Plot close i sma
matplotlib.pyplot.plot(close)
matplotlib.pyplot.plot(sma)
matplotlib.pyplot.plot(mx)
matplotlib.pyplot.plot(mn)
matplotlib.pyplot.show()
