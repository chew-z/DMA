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

entry = rules.sma_crossover(close, 40, 200, 1) #buy when MAs cross
exit = rules.sma_exit(entry) #long exit = short entry
t = zip(entry.nonzero()[0], exit.nonzero()[0]) #indexes of entry and exit paired

returns = rules.returns(t, entry, close) 
drawdowns = rules.max_drawdown2(t, entry, close) 

print "Profit ", np.sum(returns)
print "Sharpe returns", formulas.sharpe(returns)
print "Sharpe drawdowns", formulas.sharpe(drawdowns)

## Plot accumulated returns and drawdowns
matplotlib.pyplot.subplot(211)
matplotlib.pyplot.plot(np.cumsum(returns))
matplotlib.pyplot.subplot(212)
matplotlib.pyplot.plot(np.cumsum(drawdowns))
matplotlib.pyplot.show()
