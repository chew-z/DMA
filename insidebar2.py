# -*- coding: utf-8 -*-
"""
Created on Tue Sep  30 18:21:52 2014
1) import data, D1
2) identify inside bars

@author: chew-z
"""

import read_mql as read_mql
import numpy as np

# 1 import data, sync H1 with D1
csv_listD1 = read_mql.csv_to_list('./data/EURUSD1440_01.csv')

d_mat = read_mql.convert_cells_to_floats(csv_listD1, 1, 3)
closeD1 = d_mat[:, 3]
highD1 = d_mat[:, 1]
lowD1 = d_mat[:, 2]


del d_mat, csv_listD1

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

# dla każdego bar zbadaj czy jest Inside bar
# jeśli zakres start przekracza sygnał to mamy We
# a Wy to Time Exit, czyli Close po K barach

# print BarSize[100 - 5:100]
# print motherBar(100, 5)
# print BarSize[motherBar(100, 5)]
# print isMotherBar(100, 5)

K = 4
signal = np.zeros(len(closeD1))
returns = np.zeros(len(closeD1))

for i in range(K, len(closeD1)):
    if isMotherBar(i, K):
        mb = motherBar(i, K)
        if lowD1[i] < lowD1[mb]:
            signal[i] = -1
            returns[i] = -1.0 * (closeD1[i] - lowD1[mb])
        if highD1[i] > highD1[mb]:
            signal[i] = 1
            returns[i] = closeD1[i] - highD1[mb]

del mb, i
