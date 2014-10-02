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
returns = g['returns']  # import list of results - returns, sharpe etc.

PL = returns

print "Total profit ", np.sum(returns)
print "Sharpe returns", formulas.sharpe(returns)

# 1 Check P&L autocorrelation
matplotlib.pyplot.subplot(221)
matplotlib.pyplot.plot(formulas.autocorr(PL))
# 2 Plot histogram P&L
matplotlib.pyplot.subplot(222)
matplotlib.pyplot.hist(PL)
# 3 Plot cumulation of P&L
matplotlib.pyplot.subplot(223)
matplotlib.pyplot.plot(np.cumsum(PL))
# 4 Plot G vs. f - if < 1 you are waisting time
X = formulas.gvsf(PL)
matplotlib.pyplot.subplot(224)
matplotlib.pyplot.plot(X[:, 0], X[:, 1])

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
