# -*- coding: utf-8 -*-
"""
Created on Sun Jun 22 17:43:11 2014

@author: chew-z
"""

import numpy as np

def max_drawdown(buys_idx, sells_idx, close, mm= 'MIN'): 
#calculates index maximum drawdown points
    dd_index = []
    for i in xrange(len(buys_idx)):
        arr = close[buys_idx[i]:sells_idx[i]]
        if mm == 'MAX':
            dd = np.where(arr == np.amin(arr))
        else:
            dd = np.where(arr == np.amin(arr))
        dd_index = dd_index + [buys_idx[i] + dd[0][0]]
    return dd_index
    
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