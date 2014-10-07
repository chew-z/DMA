# -*- coding: utf-8 -*-
"""
Created on Mon Oct  6 20:27:37 2014
shuffling longe vector by permutating it's chunks
@author: chew-z
"""
import itertools
import read_mql as read_mql
import numpy as np
import matplotlib.pyplot as plt

# 1 import data, sync H1 with D1
csv_listD1 = read_mql.csv_to_list('./data/USDJPY1440_01.csv')

d_mat = read_mql.convert_cells_to_floats(csv_listD1, 1, 3)
closeD1 = d_mat[:, 3]
highD1 = d_mat[:, 1]
lowD1 = d_mat[:, 2]

del csv_listD1

# x is your dataset

K = 4
N = len(closeD1)
x = np.arange(N)

def chunks(l, n):
    """ Yield successive n-sized chunks from l.
    """
    for i in xrange(0, len(l), n):
        yield l[i:i+n]
        
#l1 = list( chunks(x, N//K))              # slice array into chunks
#l2 = list(itertools.permutations(l1, K)) # permutate chunks
#for a in l2:                             #for each permutation
#    print np.r_[a]                             #merge slices

# this is maybe pythonic but less redeable code
for a in itertools.permutations(chunks(x, N//K), K):
    idx = np.r_[a]
    newCloseD1 = closeD1[idx]
    plt.plot(newCloseD1)