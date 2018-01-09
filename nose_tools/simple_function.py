# -*- coding: utf-8 -*-
"""
Created on Tue Jan 09 10:25:32 2018

@author: sd835979
"""

#
# Simple function to calculate 
# the square of the square root
# of a positive number
# simple_function.py
#

from math import sqrt

def f(x):
    '''
        Function to calculate square of the square root of a number
        
        Parameters
        ===========
        x : int or float
            The input number
        
        Returns
        =======
        fx : float
             square of the square root of a number
             
        Raises
        ======
        TypeError
            if the number is neither int nor float
        ValueError
            if the number is negative
            
        Examples
        ========
        >>> f(1)
        1
        
        >>> f(10.5)
        10.5
    
    '''
    
    if type(x)!= int and type(x)!= float:
        raise TypeError('Input does not has the right type')
    if x < 0:
        raise ValueError('Input is negative')
    fx = sqrt(x) ** 2
    return fx
    
    