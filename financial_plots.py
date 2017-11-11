# -*- coding: utf-8 -*-
"""
Created on Sat Nov 11 00:51:49 2017

@author: sid
"""

import matplotlib.finance as mpf

start=(2017, 1, 1)
end=(2017,11, 10)

quotes = mpf._quotes_historical_yahoo('^GDAXI', start, end)
quotes[:2]

