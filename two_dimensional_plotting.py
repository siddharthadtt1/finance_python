# -*- coding: utf-8 -*-
"""
Created on Thu Nov 09 14:33:31 2017

@author: sd835979
"""

import numpy as np
import matplotlib as mlt
import matplotlib.pyplot as plt

np.random.seed(1000)
y = np.random.standard_normal(20)

x = range(len(y))

# plt.plot(x, y)
# plt.plot(y)
plt.plot(y.cumsum())

plt.grid(True) # adds a grid 
# plt.axis('tight') # adjusts the axis ranges
# plt.axis('off') # turns axis lines and labels off
# plt.axis('equal') # leads to equal scaling
# plt.axis('scaled') # equal scaling via dimension changes
plt.axis('tight') # Makes all data visible 
plt.axis([0, 20, -2.5, 1]) # [xmin, xmax, ymin, ymax]
