# -*- coding: utf-8 -*-
"""
1) Which horizon maximizes sharpe of returns and minimizes drawdown?
2) How to handle maximum drawdown?
3) Add geometric rate of return, Kelly's f
4) Convert RoR into dollar P&L
4) Benchmark versus sharpe of random trades

Created on Fri Jun 20 09:09:39 2014
@author: chew-z
"""
import numpy as np
import scipy.io as scio
import matplotlib.pyplot

import formulas as formulas

SENSIVITY = 0.0007
d = scio.loadmat("Close.mat") #Matlab matrix with H1Close & DMA200
close = d['C'][:,0].tolist()
dma = d['D'][:,0].tolist()
detr=(d['C'][:,0]-d['D'][:,0]).tolist() #detrended values

def drawdown(mm='MIN'): #calculates maximum drawdown
    dd_index = []
    if mm == 'MAX':
        for signal in signals:
            dd = close[signal:signal+horizon].index(max(close[signal:signal+horizon]))
            dd_index = dd_index + [signal+dd]
    else:
        for signal in signals:
            dd = close[signal:signal+horizon].index(min(close[signal:signal+horizon]))
            dd_index = dd_index + [signal+dd]
    return dd_index
    
def fuzzy_filter(k, K, T, mm='from_above'): #filters out signal with fuzzy logic
    cnt = 0
    for i in range(K):
        if (mm =='from_below') and (dma[k-i] > close[k-i]): # zamknięcia poniżej DMA
            cnt +=1
        elif (mm == 'from_above') and (dma[k-i] < close[k-i]):
            cnt +=1     
    if cnt >= T:
        return True
    else:
        return False  

def signal(mm='from_below'): #here define your entry signal logic
    start = np.where(np.abs(detr) < SENSIVITY)
    sig = []
    for s in start[0]:
         if fuzzy_filter(s, 24, 6, mm): #passing mm input parameter to filter
            sig = sig + [s]
    return np.array(sig)
    


horizon = 100*24 # time exit of your strategy - random but simple check
signals = signal('from_below') # buy when price crosses DMA up
signals = formulas.clean_signal(signals, horizon)
buys = np.take(close, signals)
sells = np.take(close, formulas.sell(signals, horizon, len(close))) #horizon+signals < len(close)
returns = (sells-buys)/buys
drawdowns = (np.take(close, drawdown('MIN'))-buys)/buys

print formulas.sharpe(returns)
print formulas.sharpe(drawdowns)
# Plot accumulated returns and drawdowns
matplotlib.pyplot.subplot(211)
matplotlib.pyplot.plot(np.cumsum(returns))
matplotlib.pyplot.subplot(212)
matplotlib.pyplot.plot(np.cumsum(drawdowns))
matplotlib.pyplot.show()
