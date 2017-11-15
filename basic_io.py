# -*- coding: utf-8 -*-
"""
Created on Tue Nov 14 17:57:22 2017

@author: sd835979
"""

import os
import numpy as np
from random import gauss
import pickle

a = [gauss(1.5, 2) for i in range(1000000)]

pkl_file_name = 'data.txt'
pkl_file = open(os.getcwd() + '\\' + pkl_file_name, 'w')
pickle.dump(a, pkl_file)
pkl_file.close()

pkl_file = open(os.getcwd() + '\\' + pkl_file_name, 'r')
b = pickle.load(pkl_file)

