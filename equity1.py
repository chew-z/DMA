# -*- coding: utf-8 -*-
"""
Created on Tue Aug  19 09:16:52 2015
1) import data from Equity.csv
2) plot equity graph
TODO - merge various ranges, plot date

@author: chew-z
"""

import read_mql as read_mql
import matplotlib.pyplot


# 1 import data and select range
csv_listEq = read_mql.csv_to_list('./data/Equity.csv', ',')
eq_mat = read_mql.convert_cells_to_floats(csv_listEq, 0, 1)
eq_t = read_mql.extract_timestamp_as_dt(csv_listEq, 0)

t = range(2250, 2450) + range(3000, 3250)
y = eq_mat[t, 1]
x = eq_t[t]

# 2 plot equity graph
fig = matplotlib.pyplot
# There is a tricky issue here
# - if you plot with x (dates) the gaps in range are filled in automatically
# - simple plot of y omits gaps in the range
#fig.plot(x, y)
fig.plot(y)
# beautify the x-labels
fig.gcf().autofmt_xdate()
fig.grid(True)
fig.title(r'Equity')
fig.show()
