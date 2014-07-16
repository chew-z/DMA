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
import matplotlib.pyplot
import scipy.io as scio
import formulas as formulas
import rules as rules

d_mat = scio.loadmat("Close.mat") #Matlab matrix with H1Close & DMA200
close = np.array(d_mat['C'][:, 0])

xi = []
yj = []
sharpe = []
for i in range(5, 100, 5):
    for j in range(i+5, 200, 5):
        entry = rules.sma_crossover(close, i, j, 1) #buy when MAs cross
        exit = rules.sma_exit(entry) #long exit = short entry
        t = zip(entry.nonzero()[0], exit.nonzero()[0]) #indexes of entry and exit paired
        returns = rules.returns(t, entry, close) 
        drawdowns = rules.max_drawdown2(t, entry, close) 
        
        if np.sum(returns) > 0.0:
            print "i= ", i, " j= ", j
            print "Total profit ", np.sum(returns)
            print "Sharpe returns", formulas.sharpe(returns)
            print "Sharpe drawdowns", formulas.sharpe(drawdowns)
            xi.append(i)
            yj.append(j)
            sharpe.append(formulas.sharpe(returns))
        
matplotlib.pyplot.subplot(211)
matplotlib.pyplot.scatter(xi, yj, marker='+', c=sharpe, cmap=matplotlib.pyplot.cm.coolwarm)
matplotlib.pyplot.subplot(212)
matplotlib.pyplot.hist(sharpe)
matplotlib.pyplot.show()
#            PL = returns
#            f = formulas.f(PL)
#
#            largest_loss = min(PL)
#            print "Optimum f: ", f
#            f_dollar = -largest_loss/f
#            print "f dollar: ", f_dollar
#            twr = formulas.TWR(PL, f)
#            print "Terminal Wealth Return = ", twr
#            g = twr ** (1.0/len(PL)) - 1
#            print "G = ", g
#            gat = g * (- largest_loss/f)
#            print "Geometric Average Trade = ", gat
    