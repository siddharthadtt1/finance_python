# -*- coding: utf-8 -*-
"""
Created on Sat Nov 11 00:51:49 2017

@author: sid
"""

import numpy as np
import pandas as pd

df = pd.DataFrame(data=[10, 20, 30, 40], columns=['numbers'], index=['a', 'b', 'c', 'd'])

df['floats'] = (1.5, 2.5, 3.5, 4.5)
df['names'] = pd.DataFrame(data=['Sid', 'Josh', 'Manuel'], index=['a', 'b', 'c'])

# Appending data works similarly. However, in the following example we see a side effect
# that is usually to be avoided — the index gets replaced by a simple numbered index

 # df.append({'numbers': 100, 'floats': 10.5, 'names':'Mikael'}, ignore_index=True)
 
 
df = df.append(pd.DataFrame({'numbers': 100, 'floats': 10.5, 'names': 'Mikael'}, index=['z',]))

# replace a column value
# df.loc[<row selection>, <column selection>]
#df.loc['c', 'names'] = 'Harsh'

# drop last row
#df.drop(df.index[len(df)-1])

# drop last n rows
#df.drop(df.tail(2).index,inplace=True) 

 # drop first n rows
#df.drop(df.head(1).index, inplace=True)
 
df.loc['d', 'names'] = 'Harsh'

# using joins
df = df.join(pd.DataFrame(data=[1, 4, 9, 16, 25], index=['a', 'b', 'c', 'd', 'y'], 
                          columns=['squares',]), how='outer')

#print df[['numbers', 'squares']].mean()
#print df[['numbers', 'squares']].std()

a = np.random.standard_normal((9, 4))

df = pd.DataFrame(a)

df.columns= [['No1', 'No2', 'No3', 'No4']]

dates = pd.date_range('2017-01-01', periods=9, freq='M')

#Parameter   Format              Description
#start       string/datetime     left bound for generating dates
#end         string/datetime     right bound for generating dates
#periods     integer/None        number of periods (if start or end is None)
#freq        string/DateOffset   frequency string, e.g., 5D for 5 days
#tz          string/None         time zone name for localized index
#normalize   bool, default None  normalize start and end to midnight
#name        string, default None name of resulting index

df.index = dates

#df.cumsum().plot(lw=2.0)
 

import matplotlib.pyplot as plt

#plt.plot(df['No1'].cumsum(), 'r', lw= 2)
df['No1'].cumsum().plot(style='r', lw= 2.)
plt.xlabel('date')
plt.ylabel('value')

# GroupBy 

df['Quarter'] = ['Q1', 'Q1', 'Q1', 'Q2', 'Q2', 'Q2', 'Q3', 'Q3', 'Q3']
groups = df.groupby('Quarter')

# group by mean
print groups.mean()

# group by max
print groups.max()

# group by size
print groups.size()

# group by with multiple columns
df['Odd_Even'] = ['Odd', 'Even', 'Odd', 'Even', 'Odd', 'Even', 'Odd', 'Even', 'Odd']

groups = df.groupby(['Quarter', 'Odd_Even'])

print groups.mean()
print groups.max()










