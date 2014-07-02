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

d_mat = scio.loadmat("Close.mat") #Matlab matrix with H1Close & DMA200
close = np.array(d_mat['C'][:, 0])

horizon = 10*24 # time exit horizon of your strategy - simple and random check
signals = rules.sma_buy(close, 50, 200, 1) # buy when MA crosses
# buys and sells should contain only nonzero elements
buys = close * signals
exits = rules.sma_exit(signals)
sells = close * exits
t = zip(buys.nonzero()[0], sells.nonzero()[0])
returns = np.zeros(len(t))
for i in xrange(len(t)):
    returns[i] = sells[t[i][1]] - buys[t[i][0]] #too complicated indexing
profit = sells.sum() - buys.sum()

#drawdowns = (np.take(close, rules.max_drawdown(signals, signals+horizon, close, 'MIN'))-buys)/buys
#
#print formulas.sharpe(returns)
#print formulas.sharpe(drawdowns)
## Plot accumulated returns and drawdowns
#matplotlib.pyplot.subplot(211)
#matplotlib.pyplot.plot(np.cumsum(returns))
#matplotlib.pyplot.subplot(212)
#matplotlib.pyplot.plot(np.cumsum(drawdowns))
#matplotlib.pyplot.show()
