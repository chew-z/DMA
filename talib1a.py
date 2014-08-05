# -*- coding: utf-8 -*-
"""
1) Testing TA-Lib and it's cpython wraper

Created on Fri Jun 27 23:09:39 2014
@author: chew-z
"""
#import numpy as np
import matplotlib.pyplot
import read_mql as mql
import formulas as formulas

d_mat = mql.convert_cells_to_floats(mql.csv_to_list('./data/USDJPY1440_01.csv'), 1, 3)
close = d_mat[:, 3]
high  = d_mat[:, 1]
low   = d_mat[:, 2]
del d_mat

f_l = formulas.f_lookbackdays(close, EMA=60)
hh, ll = formulas.f_hh_ll(f_l, high, low)  
is_recentHigh, is_recentLow = formulas.is_recent_HL(high, low, hh, ll, K=5)
is_pullbackH, is_pullbackL = formulas.is_pullback(high, low, K=5)

# wektorówki isPullback()

## Plot close i stddev
#matplotlib.pyplot.subplot(221)
#matplotlib.pyplot.plot(stdev)
#matplotlib.pyplot.title('std dev (close)')
#
#matplotlib.pyplot.subplot(222)
matplotlib.pyplot.plot(close)
matplotlib.pyplot.plot(hh)
matplotlib.pyplot.plot(ll)
matplotlib.pyplot.title('min/max close')
#
#matplotlib.pyplot.subplot(223)
#matplotlib.pyplot.plot(deltaVol)
#matplotlib.pyplot.title('delta volatility')
#
#matplotlib.pyplot.subplot(224)
#matplotlib.pyplot.hist(deltaVol)
#matplotlib.pyplot.title('histogram volatility')
#
#matplotlib.pyplot.show()
