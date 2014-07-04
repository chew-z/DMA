# -*- coding: utf-8 -*-
"""
Created on Sun Jun 22 17:43:11 2014

@author: chew-z
"""

import numpy as np
import talib as talib

def max_drawdown(buys_idx, sells_idx, close, mm= 'MIN'): 
#calculates index maximum drawdown points
    dd_index = []
    for i in xrange(len(buys_idx)):
        arr = close[buys_idx[i]:sells_idx[i]]
        if mm == 'MAX':
            dd = np.where(arr == np.amax(arr))
        else:
            dd = np.where(arr == np.amin(arr))
        dd_index = dd_index + [buys_idx[i] + dd[0][0]]
    return dd_index

def max_drawdown2(t, signals, close): 
#calculates index maximum drawdown points
#t = zip(buys.nonzero()[0], sells.nonzero()[0]) = paired indexes of entry and exit
    dd = []
    for i in xrange(len(t)):
        arr = close[t[i][0]:t[i][1]]
        sign = np.sign(arr[0])
        if sign: #if long entry look for minimum value
            ddi = np.where(arr == np.amin(arr)) #look for index of minimum
            ddd = sign * (arr[ddi[0][0]] - arr[0]) #calculate drawdown
        else:
            ddi = np.where(arr == np.amax(arr))
            ddd = sign * (arr[ddi[0][0]] - arr[0])
        dd = dd + [ddd] #drawdown is newver positive value max - 0.0
    return dd
    
def returns(t, signals, close):
#t = zip(buys.nonzero()[0], sells.nonzero()[0]) = paired indexes of entry and exit    
    returns = np.zeros(len(t))
    for i in xrange(len(t)):
        returns[i] = np.sign(signals[t[i][0]]) * (close[t[i][1]] - close[t[i][0]]) #bit too complicated indexing
    return returns
    
def fuzzy_filter(close, dma, k, K, T, mm= 'from_above'): #filters out signal with fuzzy logic
    cnt = 0
    for i in range(K ):
        if (mm == 'from_below') and (dma[k-i] > close[k-i]): # zamknięcia poniżej DMA
            cnt +=1
        elif (mm == 'from_above') and (dma[k-i] < close[k-i]):
            cnt +=1     
    if cnt >= T:
        return True
    else:
        return False  

def signal(close, dma, detr, sensivity, mm= 'from_below'): #here define your entry signal logic
    start = np.where(np.abs(detr) < sensivity)
    sig = []
    for s in start[0]:
        if fuzzy_filter(close, dma, s, 24, 6, mm): #passing mm input parameter to filter
            sig = sig + [s]
    return np.array(sig)
    
def time_exit(signals, horizon, max_length): # Simple time exits 
    temp = signals + horizon
    for i in xrange(len(temp)):    
        if temp[i] >= max_length:
            temp[i] = max_length-1 #Maximum index cannot extend beyond range of close[]
    return temp
    
def sma_exit(signals): # always in position (long exit - short entry)
    temp = np.zeros(len(signals)) 
    signal_idx = signals.nonzero()[0] #indeksy sygnałów
    for s, next_s in zip(signal_idx[:-1], signal_idx[1:]): #neat trick
    #There's no need to specify words[:-1]; zip will truncate the output to the length of the shortest arguent (in this case, the second)
        if signals[s] == signals[next_s]:   #if signal repeats itself
            break 
        else:
            temp[next_s] = signals[s]       #if signal reverses
    temp[-1] = signals[signal_idx[-1]]  #close last position at the end
    return temp
    
def clean_signal(signals, horizon): #Only first instance of signal is taken, so clean following
    x = signals[0]
    temp = [x]
    for i in range(len(signals)):
        if signals[i] > x + horizon:
            temp = temp + [signals[i]]
            x = signals[i]
    return np.array(temp)
    
def sma_crossover(close, t1=50, t2=200, filtr = 1): #simple sma crossover
    sma1 = talib.SMA(close, t1)
    sma2 = talib.SMA(close, t2)
    index1 = sma1 > sma2
    index2 = sma2 > sma1
    signal = np.zeros(len(close))
    for i in range(filtr, len(close)):
        if (index1[i] and index2[i-filtr]): #not infallable logic
            signal[i] = 1.0
        elif (index2[i] and index1[i-filtr]):
            signal[i] = -1.0
#clean the signal [exceptions,]
    return signal