# -*- coding: utf-8 -*-
"""
1) Which horizon maximizes sharpe of returns and minimizes drawdown?
2) How to handle maximum drawdown?
3) 
4) Convert RoR into dollar P&L
4) Benchmarking versus sharpe(random trades)

Created on Fri Jun 20 09:09:39 2014
@author: chew-z
"""
# To ignore numpy errors:
#     pylint: disable=E1101
import numpy as np
import scipy.io as scio
import matplotlib.pyplot

import formulas as formulas
import rules as rules

SENSIVITY = 0.0007
d_mat = scio.loadmat("Close.mat") #Matlab matrix with H1Close & DMA200
close = np.array(d_mat['C'][:, 0])
dma = np.array(d_mat['D'][:, 0]) #tolist()
detr=(d_mat['C'][:, 0]-d_mat['D'][:, 0]) #detrended values
    
#for i in xrange(1,30,5):
#    print formulas.ror2dolar(0.25, 1.0, float(i))

horizon = 100*24 # time exit of your strategy - random but simple check
signals = rules.signal(close, dma, detr, SENSIVITY, 'from_below') # buy when price crosses DMA up
signals = formulas.clean_signal(signals, horizon)
buys = np.take(close, signals)
sells = np.take(close, formulas.sell(signals, horizon, len(close))) #horizon+signals < len(close)
returns = (sells-buys)/buys
drawdowns = (np.take(close, rules.max_drawdown(signals, signals+horizon, close, 'MIN'))-buys)/buys

print formulas.sharpe(returns)
print formulas.sharpe(drawdowns)
# Plot accumulated returns and drawdowns
matplotlib.pyplot.subplot(211)
matplotlib.pyplot.plot(np.cumsum(returns))
matplotlib.pyplot.subplot(212)
matplotlib.pyplot.plot(np.cumsum(drawdowns))
matplotlib.pyplot.show()
