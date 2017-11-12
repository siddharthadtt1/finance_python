# -*- coding: utf-8 -*-
"""
Created on Sat Nov 11 00:51:49 2017

@author: sid
"""

import pandas_datareader.data as web
import numpy as np
import pandas as pd


AAPL = web.DataReader(name='AAPL', data_source='yahoo', start='2005-1-1')
#AAPL['Close'].plot(figsize=(8,5), style='r', lw=2)

AAPL['Ret_Loop'] = 0.0
for i in range(1, len(AAPL)):
    AAPL['Ret_Loop'][i] = np.log(AAPL['Close'][i]/AAPL['Close'][i-1])


print AAPL[['Close', 'Ret_Loop']].tail()

AAPL['Return'] = np.log(AAPL['Close'] / AAPL['Close'].shift(1))

#print AAPL[['Close', 'Ret_Loop', 'Return']].tail()

# delete AAPL['Ret_Loop'] column 
del AAPL['Ret_Loop']

#AAPL[['Close', 'Return']].plot(subplots = True, style='b', figsize=(8,5))

AAPL['42d'] = pd.rolling_mean(AAPL['Close'], window=42)
AAPL['252d'] = pd.rolling_mean(AAPL['Close'], window=252)

#AAPL[['Close', '42d', '252d']].plot(figsize=(8,5))
AAPL[['Close', '42d', '252d']].plot(subplots=True, style='b', figsize=(8, 7))








