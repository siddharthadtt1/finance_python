# -*- coding: utf-8 -*-
"""
Created on Thu Nov 09 14:33:31 2017

@author: sd835979
"""

import numpy as np
import matplotlib as mlt
import matplotlib.pyplot as plt

#np.random.seed(1000)
#y = np.random.standard_normal(20)
#
#x = range(len(y))

# plt.plot(x, y)
# plt.plot(y)
# plt.plot(y.cumsum())

# plt.grid(True) # adds a grid 
# plt.axis('tight') # adjusts the axis ranges
# plt.axis('off') # turns axis lines and labels off
# plt.axis('equal') # leads to equal scaling
# plt.axis('scaled') # equal scaling via dimension changes
# plt.axis('tight') # Makes all data visible 
# plt.axis([0, 20, -2.5, 1]) # [xmin, xmax, ymin, ymax]

# plt.xlim(-1, 20)
# plt.ylim(  np.min(y.cumsum()) - 1
#         , np.max(y.cumsum()) + 1)

#plt.figure(figsize=(7, 4))
#plt.plot(y.cumsum(), 'b', lw=1.5)

#g Green
#r Red
#c Cyan
#m Magenta
#y Yellow
#k Black
#w White

#plt.plot(y.cumsum(), 'ro')

#Character Symbol
#-              Solid line style
#—              Dashed line style
#-.             Dash-dot line style
#:              Dotted line style
#.              Point marker
#,              Pixel marker
#o              Circle marker
#v              Triangle_down marker
#^              Triangle_up marker
#<               Triangle_left marker
#>               Triangle_right marker
#1               Tri_down marker
#2               Tri_up marker
#3               Tri_left marker
#4               Tri_right marker
#s               Square marker
#p               Pentagon marker
#*               Star marker
#h               Hexagon1 marker
#H               Hexagon2 marker
#+               Plus marker
#x               X marker
#D               Diamond marker
#d               Thin diamond marker
#|               Vline marker

#Legend location
#Loc     Description
#Empty   Automatic
#0       Best possible
#1       Upper right
#2       Upper left
#3       Lower left
#4       Lower right
#5       Right
#6       Center left
#7       Center right
#8       Lower center
#9       Upper center
#10      Center

#plt.grid(True)
#plt.axis('tight')
#
#plt.xlabel('index')
#plt.ylabel('value')
#plt.title('A simple plot')
#


np.random.seed(2000)
y = np.random.standard_normal((20, 2)).cumsum(axis=0)

#plt.figure(figsize=(7,4))

# draw two lines
# plt.plot(y, 'b', lw=1.5)

#plt.plot(y[:, 0], 'b', lw=1.5, label='1st')
#plt.plot(y[:, 1], 'y', lw= 1.5, label='2nd')

# draw orange circle
#plt.plot(y[:,0], 'ro')
#plt.plot(y[:, 1], 'g^')
#
#plt.legend(loc=0)
#
#plt.grid(True)
#plt.axis('tight')
#plt.xlabel('index')
#plt.ylabel('value')
#plt.title('Simple plot')

#fig, ax1 = plt.subplots()
#plt.plot(y[:, 0], 'b', lw=1.5, label='1st')
#plt.plot(y[:, 0], 'ro')
#plt.grid(True)
#plt.axis('tight')
#plt.legend(loc=8)
#plt.xlabel('index')
#plt.ylabel('value 1st')
#plt.title('Simple plot')
#
#ax2 = ax1.twinx()
#plt.plot(y[:, 1], 'y', lw=1.5, label='2nd')
#plt.plot(y[:, 1], 'g^')
#plt.legend(loc=0)
#plt.ylabel('value 2nd')

#plt.figure(figsize=(7,5))
#
#plt.subplot(211)
#plt.grid(True)
#plt.plot(y[:, 0], 'b', lw=1.5, label='1st')
#plt.plot(y[:, 0], 'ro', lw=1.5)
#plt.legend(loc=0)
#plt.axis('tight')
#plt.xlabel('index')
#plt.ylabel('value')
#plt.title('Simple plot')
#
#plt.subplot(212)
#plt.grid(True)
#plt.plot(y[:, 1], 'y', lw=1.5, label='2nd')
#plt.plot(y[:, 1], 'g^', lw=1.5)
#plt.legend(loc=0)
#plt.axis('tight')
#plt.xlabel('index')
#plt.ylabel('value')

plt.figure(figsize=(9, 4))

plt.subplot(121)
plt.plot(y[:, 0], lw=1.5, label='1st')
plt.plot(y[:, 0], 'ro')
plt.legend(loc=0)
plt.xlabel('index')
plt.ylabel('value')
plt.grid(True)
plt.axis('tight')
plt.title('1st Data Set')

plt.subplot(122)
plt.bar(np.arange(len(y)), y[:, 1], color='g', width=0.5, label='2nd')
plt.grid(True)
plt.axis('tight')
plt.legend(loc=0)
plt.xlabel('index')
plt.ylabel('value')
plt.title('2nd Data Set')


