# -*- coding: utf-8 -*-
"""
Created on Wed Oct  1 14:54:52 2014
1) visualize insiderbar.py

@author: chew-z
"""
import numpy as np
import matplotlib.pyplot
import formulas as formulas

g = globals()  # read global variables
PL_arr = g['PL']  # import list of results - returns, sharpe etc.
fo = []
fd = []

for PL in PL_arr:

    returns = PL
    print "Total profit ", np.sum(returns)
    print "Sharpe returns", formulas.sharpe(returns)
    
    # 1 Check P&L autocorrelation
    fig = matplotlib.pyplot.subplot(221)
    fig.plot(formulas.autocorr(PL))
    fig.set_title(r'Autocorrelation')
    # 2 Plot histogram P&L
    fig = matplotlib.pyplot.subplot(222)
    fig.hist(PL)
    fig.set_title(r'Histogram')
    # 3 Plot cumulation of P&L
    fig = matplotlib.pyplot.subplot(223)
    fig.plot(np.cumsum(PL))
    fig.set_title(r'Cumulated returns')
    # 4 Plot G vs. f - if < 1 you are waisting time
    X = formulas.gvsf(PL)
    fig = matplotlib.pyplot.subplot(224)
    fig.plot(X[:, 0], X[:, 1])
    fig.set_title(r'G vs f')
    
    matplotlib.pyplot.show()
    
    f = formulas.f(PL)
    
    largest_loss = min(PL)
    print "Optimum f: ", f
    f_dollar = -largest_loss / f
    print "f dollar: ", f_dollar
    twr = formulas.TWR(PL, f)
    print "Terminal Wealth Return = ", twr
    g = twr ** (1.0 / len(PL)) - 1
    print "G = ", g
    gat = g * (- largest_loss / f)
    print "Geometric Average Trade = ", gat
    print "Largest win = ", returns.max(), " @ ", returns.argmax()
    index_sorted = np.argsort(returns)
    #print "Largest losses", zip(index_sorted[0:5], returns[index_sorted[0:5]])
    #print "Largest win ", zip(index_sorted[-5:-1], returns[index_sorted[-5:-1]])
    print "Average return = ", returns.mean()
    fo.append(f)
    fd.append(f_dollar)

del twr, index_sorted, g, gat, f_dollar, f, X, largest_loss