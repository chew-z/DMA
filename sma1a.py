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
#import matplotlib.pyplot
#import scipy.io as scio
import formulas as formulas
import rules as rules
import read_mql as mql 

#d_mat = scio.loadmat("Close.mat") #Matlab matrix with H1Close & DMA200
d_mat = mql.convert_cells_to_floats(mql.csv_to_list('./EURUSD60_01.csv'), 1, 3)
close = d_mat[:, 3]
del d_mat

xi = []
yj = []
results = []
for i in range(5, 100, 1):
    for j in range(i+5, 200, 1):
        entry = rules.sma_crossover(close, i, j, 1) #buy when MAs cross
        exit = rules.sma_exit(entry) #long exit = short entry
        t = zip(entry.nonzero()[0], exit.nonzero()[0]) #indexes of entry and exit paired
        returns = rules.returns(t, entry, close) 
        drawdowns = rules.max_drawdown2(t, entry, close) 
        
        if np.sum(returns) > 0.0:
            print "i= ", i, " j= ", j

            xi.append(i)
            yj.append(j)
            
            PL = returns
            f = formulas.f(PL)
            largest_loss = min(PL)
            f_dollar = -largest_loss/f
            twr = formulas.TWR(PL, f)
            g = twr ** (1.0/len(PL)) - 1
            gat = g * (- largest_loss/f)
            results.append([np.sum(returns), formulas.sharpe(returns), formulas.sharpe(drawdowns),
                            f, twr, g, gat])
#            print "Total profit ", np.sum(returns)
#            print "Sharpe returns", formulas.sharpe(returns)
#            print "Sharpe drawdowns", formulas.sharpe(drawdowns)
#            print "Optimum f: ", f
#            print "f dollar: ", f_dollar
#            print "Terminal Wealth Return = ", twr
#            print "G = ", g
#            print "Geometric Average Trade = ", gat            

results = np.array(results)
#remove unused variables from global namespace
del i, j, t, entry, exit
del returns, drawdowns, PL, largest_loss, f, f_dollar, twr, g, gat
#Visualization of the results moved to visualize1.py



    