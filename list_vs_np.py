# -*- coding: utf-8 -*-
"""
Created on Thu Nov 09 13:06:21 2017

@author: sd835979
"""
import numpy as np
import sys
import time

def compute_time(l1, l2, dtype='None'):
    start = time.time()
    if dtype == 'list':
        [(x+y) for x,y in zip(l1, l2)]
    else:
        l1 + l2
    return time.time() - start

def test_list(limit):
    
    # test memory efficiency
    l1 = range(limit)
    print('Size of list is : %d' % (sys.getsizeof(5)* sys.getsizeof(l1)))
    
    # test speed of computation
    l2 = range(limit)
    time_taken = compute_time(l1, l2, 'list')
    print('Time taken to perform a operation in list : %f ' %time_taken )
    
def test_np_ndarray(limit):
    
    # test memory efficiency
    arr1 = np.arange(limit)
    print('Size of np array is : %d ' % (arr1.size* arr1.itemsize) )   
    
    arr2 = np.arange(limit)
    time_taken = compute_time(arr1, arr2)
    print('Time taken to perform a operation in np array : %f ' %time_taken )
    
    
# limit 
LIMIT = 1000000


test_list(LIMIT)
test_np_ndarray(LIMIT)