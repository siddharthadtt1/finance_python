# -*- coding: utf-8 -*-
"""
Created on Tue Nov 21 01:01:46 2017

@author: sid
"""

import numpy as np
import os
import pandas as pd

path = os.getcwd() + '\\'
file_name = 'data_1.csv'

rows = 5000
a = np.random.standard_normal((rows, 5))

t = pd.date_range(start='2014/1/1', freq='H', periods=rows)

csv_file = open(path + file_name, 'w')
header = 'date,no1,no2,no3,no4,no5\n'
csv_file.write(header)

for t_, (no1,no2,no3,no4,no5) in zip(t, a):
    s = '%s,%f,%f,%f,%f,%f\n' % (t_, no1, no2, no3, no4, no5)
    csv_file.write(s)
    
csv_file.close()

csv_file = open(path + file_name, 'r')

# 1 to print csv file contents
for i in range(5):
    print csv_file.readline()
    
# 2 to print csv file contents
csv_file_contents = csv_file.readlines()

for line in csv_file_contents[:5]:
    print line
    
csv_file.close()
