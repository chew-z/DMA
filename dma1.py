# -*- coding: utf-8 -*-
"""
1) Which horizon maximizes sharpe of returns and minimizes drawdown?
2) How to handle maximum drawdown?
3) Add geometric rate of return
4) Benchmark versus sharpe of random trade

Created on Fri Jun 20 09:09:39 2014
@author: chew-z
"""
import numpy as np
import scipy.io as scio
import matplotlib.pyplot

d = scio.loadmat("Close.mat") #Matlab matrix with H1Close & DMA200
close = d['C'][:,0].tolist()
dma = d['D'][:,0].tolist()
detr=(d['C'][:,0]-d['D'][:,0]).tolist() #detrended values

def sharpe(returns): # Sharpe ratio
    m=np.mean(returns)
    s=np.std(returns)
    return float(m)/s
    
def dd(mm='MIN'): #calculates maximum drawdown
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
    
def fuzzy_filter(k, K, T, mm='above'): #filters out signal with fuzzy logic
    cnt = 0
    for i in range(K):
        if (mm =='below') and (dma[k-i] > close[k-i]): # zamknięcia poniżej DMA
            cnt +=1
        elif (mm == 'above') and (dma[k-i] < close[k-i]):
            cnt +=1     
    if cnt >= T:
        return True
    else:
        return False  

def signal(mm='below'): #here define your entry signal logic
    start = np.where(np.abs(detr) < 0.0005)
    sig = []
    for s in start[0]:
        if fuzzy_filter(s, 24, 6, mm):
            sig = sig + [s]
    return(np.array(sig))

horizon = 100*24 # time exit of your strategy - random but simple check
signals = signal('above')
buys = np.take(close, signals)
sells = np.take(close, horizon+signals)
returns = (sells-buys)/buys
drawdowns = (np.take(close, dd())-buys)/buys

print sharpe(returns)
print sharpe(drawdowns)
# Plot accumulated returns and drawdowns
matplotlib.pyplot.subplot(211)
matplotlib.pyplot.plot(np.cumsum(returns))
matplotlib.pyplot.subplot(212)
matplotlib.pyplot.plot(np.cumsum(drawdowns))
matplotlib.pyplot.show()
