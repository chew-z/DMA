# -*- coding: utf-8 -*-
"""
Created on Mon Oct  6 20:27:37 2014
shuffling longe vector by permutating it's chunks
@author: chew-z
"""

import numpy as np
import itertools
# x is your dataset

K = 4
N = 25
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
    print np.r_[a]