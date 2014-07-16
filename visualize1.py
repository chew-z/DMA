# -*- coding: utf-8 -*-
"""
Visualize results of testing sma strategy sma1a.py
Created on Wed Jul 16 12:49:10 2014

@author: chew-z
"""
import matplotlib.pyplot

g = globals()   #read global variables
xi = g['xi']    #import xi - first sma of profitable results
yj = g['yj']    #import yj - second sma of profitable results
results = g['results']  #import list of results - returns, sharpe etc.

sharpe = results[:, 1]
profit = results[:, 0]
f = results[:, 3]
            
matplotlib.pyplot.subplot(221)
matplotlib.pyplot.scatter(xi, yj, marker='+', c=sharpe, cmap=matplotlib.pyplot.cm.coolwarm)
matplotlib.pyplot.title('sharpe returns colormap')
matplotlib.pyplot.grid(True)

matplotlib.pyplot.subplot(222)
matplotlib.pyplot.hist(sharpe)
matplotlib.pyplot.title('histogram sharpe')

matplotlib.pyplot.subplot(223)
matplotlib.pyplot.scatter(xi, yj, marker='+', c=f, cmap=matplotlib.pyplot.cm.coolwarm)
matplotlib.pyplot.title('optimum f colormap')
matplotlib.pyplot.grid(True)

matplotlib.pyplot.subplot(224)
matplotlib.pyplot.hist(f)
matplotlib.pyplot.title('histogram f')

matplotlib.pyplot.show()