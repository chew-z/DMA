# -*- coding: utf-8 -*-
"""
Created on Wed Jul 16 09:17:43 2014

@author: chew-z
"""
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

csv_list = csv_to_list('./EURUSD60_01.csv')
y = convert_cells_to_floats(csv_list, 1, 3)

print('first 3 rows:')
for i in range(1, 4):
    print(y[i])