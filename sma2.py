# -*- coding: utf-8 -*-
"""
1) sma crossover part II
2) 

Created on Fri Jul 05 19:44:39 2014
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

entry = rules.sma_crossover(close, 20, 30, 1) #buy when MAs cross
exit = rules.sma_exit(entry) #long exit = short entry
t = zip(entry.nonzero()[0], exit.nonzero()[0]) #indexes of entry and exit paired

returns = rules.returns(t, entry, close) 
drawdowns = rules.max_drawdown2(t, entry, close) 
PL = returns

print "Total profit ", np.sum(returns)
print "Sharpe returns", formulas.sharpe(returns)
print "Sharpe drawdowns", formulas.sharpe(drawdowns)

#1 Check P&L autocorrelation
matplotlib.pyplot.subplot(221)
matplotlib.pyplot.plot(formulas.autocorr(PL))
#2 Plot histogram P&L
matplotlib.pyplot.subplot(222)
matplotlib.pyplot.hist(PL)
#3 Plot cumulation of P&L
matplotlib.pyplot.subplot(223)
matplotlib.pyplot.plot(np.cumsum(PL))
#4 Plot G vs. f - if < 1 you are waisting time
X = formulas.gvsf(PL)
matplotlib.pyplot.subplot(224)
matplotlib.pyplot.plot(X[:,0], X[:,1]) 

matplotlib.pyplot.show()

f = formulas.f(PL)

largest_loss = min(PL)
print "Optimum f: ", f
f_dollar = -largest_loss/f
print "f dollar: ", f_dollar
twr = formulas.TWR(PL, f)
print "Terminal Wealth Return = ", twr
g = twr ** (1.0/len(PL)) - 1
print "G = ", g
gat = g * (- largest_loss/f)
print "Geometric Average Trade = ", gat