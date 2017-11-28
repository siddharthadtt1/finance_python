# -*- coding: utf-8 -*-
"""
Created on Tue Nov 28 00:00:24 2017

@author: sid
"""

import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return np.sin(x) + 0.5 * x;

def get_x_val():
    return np.linspace(-2 * np.pi, 2 * np.pi, 50)

def approx_def():
    x = get_x_val()
    plt.plot(x, f(x), 'b')
    plt.grid(True)
    plt.xlabel('x')
    plt.ylabel('f(x)')
    
def regression_def():
    x = get_x_val()
    reg = np.polyfit(x, f(x), deg=7)
    ry = np.polyval(reg, x)
    plt.plot(x, f(x), 'b', label='f(x)')
    plt.plot(x, ry, 'r.', label='regression')
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.grid(True)
    plt.legend(loc=0)
    print np.allclose(ry, f(x))
    print (np.sum(f(x) - ry) ** 2)/ len(x)
    
#approx_def()
regression_def()