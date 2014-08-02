# -*- coding: utf-8 -*-
"""
1) Testing TA-Lib and it's cpython wraper

Created on Fri Jun 27 23:09:39 2014
@author: chew-z
"""
import numpy as np
import matplotlib.pyplot
import talib
import read_mql as mql

d_mat = mql.convert_cells_to_floats(mql.csv_to_list('./data/USDPLN1440_01.csv'), 1, 3)
close = d_mat[:, 3]
del d_mat

EMA = 60

deltaVol = np.zeros(len(close))

stdev = talib.STDDEV(close, EMA)
mx = talib.MAX(close, 20)
mn = talib.MIN(close, 20)

z = zip(stdev[1:], stdev)
i = 1
for y, x in z:
    deltaVol[i] = np.log(y/x)
    i += 1
del x, y, z, i

deltaVol = np.nan_to_num(deltaVol)
dv = deltaVol[EMA:]
print np.std(dv), np.mean(dv)

# Plot close i stddev
matplotlib.pyplot.subplot(221)
matplotlib.pyplot.plot(stdev)
matplotlib.pyplot.title('std dev (close)')

matplotlib.pyplot.subplot(222)
matplotlib.pyplot.plot(close)
matplotlib.pyplot.plot(mx)
matplotlib.pyplot.plot(mn)
matplotlib.pyplot.title('min/max close')

matplotlib.pyplot.subplot(223)
matplotlib.pyplot.plot(deltaVol)
matplotlib.pyplot.title('delta volatility')

matplotlib.pyplot.subplot(224)
matplotlib.pyplot.hist(deltaVol)
matplotlib.pyplot.title('histogram volatility')

matplotlib.pyplot.show()
