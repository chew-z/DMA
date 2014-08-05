# -*- coding: utf-8 -*-
"""
Created on Mon Aug  4 20:33:02 2014
checks read_mql.sync() - syncing bars from different timeframes
@author: chew-z
"""
import read_mql as read_mql
import datetime

csv_list1 = read_mql.csv_to_list('./data/EURUSD60_01.csv')
csv_list2 = read_mql.csv_to_list('./data/EURUSD1440_01.csv')

D1, H1, s = read_mql.sync(csv_list1, csv_list2)
del csv_list1, csv_list2

for i in range(2400, 2405):
    t = s[i]
    print datetime.datetime.utcfromtimestamp(D1[i])  # -1 ??!
    print datetime.datetime.utcfromtimestamp(H1[t[0]])
    print datetime.datetime.utcfromtimestamp(H1[t[1]])
    print t[1] - t[0]
    # print "\n"
