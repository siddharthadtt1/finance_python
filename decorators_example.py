# -*- coding: utf-8 -*-
"""
Created on Tue Jan 09 22:16:21 2018

@author: sid
"""

#
# Simple example to demonstrate 
# use of decorators in Python for logging
# decorators_example.py
#

import time

def time_it(func):
    '''
        Decorator function to compute time taken for a calculation
        
        Parameters
        ==========
        func : function
                function for which the time taken is to be calculated
        
        Returns
        =======
        result : array of numbers 

    '''
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        
        print func.__name__ , ' took time : ', ((end-start) * 1000) , 'ms'
        
        return result
    return wrapper
        

@time_it
def calc_square(arr):
    '''
        Function to calculate square for a range of numbers
        
        Parameters
        ==========
        arr : range of int 
            input range of numbers 
        
        Returns
        =======
        result : float
                returns the square of the range of numbers
        
    '''
    
    result = []
    for number in arr:
        result.append(number * number)
    
    return result

@time_it
def calc_cube(arr):
    '''
        Function to calculate cube for a range of numbers
        
        Parameters
        ==========
        arr : range of int 
            input range of numbers 
        
        Returns
        =======
        result : float
                returns the cube of the range of numbers
        
    '''
    result = []
    for number in arr:
        result.append(number * number * number)

    return result

arr = range(1, 100000)

square_result = calc_square(arr)
cube_result = calc_cube(arr)





