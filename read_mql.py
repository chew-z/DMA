# -*- coding: utf-8 -*-
"""
Created on Wed Jul 16 09:17:43 2014

@author: chew-z
"""
from datetime import datetime
import bisect
import csv
import numpy as np


def csv_to_list(csv_file, delimiter=';'):
    """
    Reads in a CSV file and returns the contents as list,
    where every row is stored as a sublist, and each element
    in the sublist represents 1 cell in the table.
    """
    with open(csv_file, 'r') as csv_con:
        reader = csv.reader(csv_con, delimiter=delimiter)
        return list(reader)


def convert_cells_to_floats(lista, body_starts=1, col_starts=3):

    result = []
    for row in lista[body_starts:]:
        result.append(map(float, row))
    return np.array(result)[:, col_starts:]


def csv_to_pl(csv_file, delimiter='\t'):
    lista = csv_to_list('./data/StrategyTester2.csv', delimiter)
    A = []
    D = []
    for row in lista:
        r = map(float, row[3:])
        sdt = row[1]
        if (r[-2] != 0.00):
            A.append(r[-2])
            D.append(datetime.strptime(sdt, '%Y.%m.%d %H:%M'))
    return np.array(A), D


def sync(csv_listH, csv_listD):
# if you would like to sync different timeframes like D1 and H1
# returns array of indexes of 1st and last bar of H1 in D1 or zeros
# works OK and is fast but logic seems tricky with bisect. I liked tuples version
# check results with sync1.py
    H1 = np.zeros(len(csv_listH) - 1).astype(int)
    i = 0
    for row in csv_listH[1:]:
        st = row[1]  # 2nd column contains datetime of bar start = Time[]
        dt = int(st)
        H1[i] = dt
        i += 1

    D1 = np.zeros(len(csv_listD) - 1).astype(int)
    i = 0
    for row in csv_listD[1:]:
        st = row[1]  # 2nd column contains datetime of bar start = Time[]
        dt = int(st)
        D1[i] = dt
        i += 1

    n = len(D1)
    l = len(H1)
    z = zip(range(n), D1, D1[1:])
    #s = []
    s = np.zeros((n, 2), int)
    t2 = 0
    for i, d1, d2 in z:
    # third argument in bisect_() is the starting point of our search = quicker
        t1 = bisect.bisect_right(H1, d1, t2)  # index to the right of d1 in H1
        t2 = bisect.bisect_left(H1, d2, t1)  # index to the left of d2 in H1
        if t1:
            t1 -= 1  # so shift(-1) gives exactly d1 index in H1
        if t2:
            t2 -= 1  # so shift(-1) gives exactly last index before d2 in H1
        if t1 != t2:
            s[i, 0] = t1
            s[i, 1] = t2
        #t = t1, t2
        # s.append(t)
    #t = 0, 0; s.append(t)
    return D1, H1, s


def sync2(csv_listH, csv_listD):
# if you would like to sync different timeframes like D1 and H1
# returns array of indexes of 1st and last bar of H1 in D1 or zeros
# np.where version seems more explicit but 5-12 times slower
# check results with sync1.py
    H1 = np.zeros(len(csv_listH) - 1).astype(int)
    i = 0
    for row in csv_listH[1:]:
        st = row[1]  # 2nd column contains datetime of bar start = Time[]
        dt = int(st)
        H1[i] = dt
        i += 1

    D1 = np.zeros(len(csv_listD) - 1).astype(int)
    i = 0
    for row in csv_listD[1:]:
        st = row[1]  # 2nd column contains datetime of bar start = Time[]
        dt = int(st)
        D1[i] = dt
        i += 1

    n = len(D1)
    z = zip(range(n), D1, D1[1:])
    s = np.zeros((n, 2), int)
    for i, d1, d2 in z:
        good = np.where((H1 >= d1) & (H1 < d2))
        if good[0].size:
            s[i, 0] = good[0][0]
            s[i, 1] = good[0][-1]
    return D1, H1, s


#pl, d = csv_to_pl('./data/StrategyTester2.csv')
# print(pl)

#csv_list = csv_to_list('./data/EURUSD60_01.csv')
#y = convert_cells_to_floats(csv_list, 1, 3)

# print('first 3 rows:')
# for i in xrange(1, 4):
#    print(y[i])
