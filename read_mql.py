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
    return np.array(result)[:, col_starts: ]
    
def csv_to_pl(csv_file, delimiter = '\t'):
    lista = csv_to_list('./data/StrategyTester2.csv', delimiter);
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
    H1 = np.zeros(len(csv_listH)-1).astype(int)
    i = 0
    for row in csv_listH[1:]:
        st = row[1]
        dt = int(st)
        H1[i] = dt
        i += 1
    
    D1 = np.zeros(len(csv_listD)-1).astype(int)
    i = 0
    for row in csv_listD[1:]:
        st = row[1]
        dt = int(st)
        D1[i] = dt
        i += 1
  
    z = zip(D1, D1[1:])
    t = 0, 0
    s = []
    s.append(t)
    t2 = 0
    for d1, d2 in z:
        t1 = bisect.bisect_right(H1, d1, t2)
        t2 = bisect.bisect_left(H1, d2, t1)
        if t1:
            t1 -= 1
        if t2:
            t2 -= 1
        t = t1, t2
        s.append(t)
    
    return D1, H1, s, z
# 

#pl, d = csv_to_pl('./data/StrategyTester2.csv')
#print(pl)

#csv_list = csv_to_list('./data/EURUSD60_01.csv')
#y = convert_cells_to_floats(csv_list, 1, 3)

# print('first 3 rows:')
# for i in xrange(1, 4):
#    print(y[i])
