# -*- coding: utf-8 -*-
"""
Created on Sat Nov 11 00:51:49 2017

@author: sid
"""

import pandas_datareader.data as web


DAX = web.DataReader(name='HUL', data_source='yahoo', start='2000-1-1')
print DAX.info()

print DAX

DAX['Close'].plot(figsize=(8, 5))