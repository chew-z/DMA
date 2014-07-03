# -*- coding: utf-8 -*-
"""
1) Simple sma crossover, short entry = long exit
2) 

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

signals = rules.sma_crossover(close, 20, 200, 1) #buy when MAs cross
exits = rules.sma_exit(signals) #long exit = short entry
t = zip(signals.nonzero()[0], exits.nonzero()[0]) #indexes of entry and exit paired

returns = rules.returns(t, close) #think it through (signs?)
drawdowns = rules.max_drawdown2(t, signals, close) #think it through (signs?)

print formulas.sharpe(returns)
print formulas.sharpe(drawdowns)
profits = np.cumsum(returns)
## Plot accumulated returns and drawdowns
matplotlib.pyplot.subplot(211)
matplotlib.pyplot.plot(np.cumsum(returns))
matplotlib.pyplot.subplot(212)
matplotlib.pyplot.plot(np.cumsum(drawdowns))
matplotlib.pyplot.show()
