# -*- coding: utf-8 -*-
"""
Created on Tue Sep  30 18:21:52 2014
1) import data, D1
2) identify inside bars
@author: chew-z
"""

import read_mql as read_mql
import itertools
import numpy as np

# 1 import data, sync H1 with 
csv_listD1 = read_mql.csv_to_list('./data/USDJPY1440_03a.csv')

d_mat = read_mql.convert_cells_to_floats(csv_listD1, 1, 3)
openD1 = d_mat[:, 0]
highD1 = d_mat[:, 1]
lowD1 = d_mat[:, 2]
closeD1 = d_mat[:, 3]

del csv_listD1, d_mat

# 2 identify inside bars
BarSize = highD1 - lowD1

def motherBar(start, K):
# zwraca indeks największej świecy
    x = BarSize[start - K:start].argmax()
    return x + (start - K)


def isMotherBar(start, K):
# badamy będąc w momencie start (czyli start=0 w MQL#
# błąd polega na tym, że operujemy tylko BarSize a nie przesłonięciem!
    mb = motherBar(start, K)
    if mb < start - 1 and lowD1[mb] < lowD1[start - 1] and highD1[mb] > highD1[start - 1]:
        return True

    return False
    
def chunks(l, n):
    """ Yield successive n-sized chunks from l.
    """
    for i in xrange(0, len(l), n):
        yield l[i:i+n]

# dla każdego bar zbadaj czy jest Inside bar
# zakres start bar[0] przekracza Hi/Lo Motherbar to sygnał
# a Time Exit na zamknięcie, czyli Close

k = 4 # number of chunks we split the data
N = len(closeD1)
x = np.arange(N)

K = 4
PL = []
for a in itertools.permutations(chunks(x, N//k), k):
    signal = np.zeros(len(closeD1))
    returns = np.zeros(len(closeD1))
    idx = np.r_[a] # new splited and permutated index
    newOpenD1 = openD1[idx]
    newHighD1 = highD1[idx]
    newLowD1 = lowD1[idx]
    newCloseD1 = closeD1[idx]
    
    for i in range(K, len(newCloseD1)):
        if isMotherBar(i, K):
            mb = motherBar(i, K)
            if newLowD1[i] < newLowD1[mb] and newOpenD1[i] > newLowD1[mb] :
                signal[i] = -1
                returns[i] = -1.0 * (newCloseD1[i] - newLowD1[mb])
            if newHighD1[i] > newHighD1[mb] and newOpenD1[i] < newHighD1[mb]:
                signal[i] = 1
                returns[i] = newCloseD1[i] - newHighD1[mb]
    
    PL.append(returns)
    print np.sum(returns)    


del mb, a, i, k, x, idx, K, N, BarSize, signal
del lowD1, highD1, newHighD1, newLowD1, closeD1, newCloseD1, openD1, newOpenD1
