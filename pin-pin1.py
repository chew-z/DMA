# -*- coding: utf-8 -*-
"""
Created on Tue Aug  5 14:48:52 2014
1) import data, sync H1 wih D1
2) find recent H/L
3) find isPullback - on D1 or better H1
4) play with parameters
5) is signal significant?
6) visualize results (with different script)
@author: chew-z
"""

import read_mql as read_mql
import formulas as formulas

# 1 import data, sync H1 with D1
csv_listH1 = read_mql.csv_to_list('./data/EURUSD60_01.csv')
csv_listD1 = read_mql.csv_to_list('./data/EURUSD1440_01.csv')

d_mat = read_mql.convert_cells_to_floats(csv_listH1, 1, 3)
closeH1 = d_mat[:, 3]
highH1 = d_mat[:, 1]
lowH1 = d_mat[:, 2]

d_mat = read_mql.convert_cells_to_floats(csv_listD1, 1, 3)
closeD1 = d_mat[:, 3]
highD1 = d_mat[:, 1]
lowD1 = d_mat[:, 2]

D1, H1, s = read_mql.sync(csv_listH1, csv_listD1)

del d_mat, csv_listD1, csv_listH1

# 2 find recent H/L
f_l = formulas.f_lookbackdays(closeD1, EMA=60)
hhD1, llD1 = formulas.f_hh_ll(f_l, highD1, lowD1)
is_recentHigh, is_recentLow = formulas.is_recent_HL(
    highD1, lowD1, hhD1, llD1, K=5)
# 3 find isPullback - on D1 or better H1
# ! this should be reworked using H1 !
is_pullbackH, is_pullbackL = formulas.is_pullback(highD1, lowD1, K=5)

# signal = isPullback, SL = ATR, trailing, exit = ?

