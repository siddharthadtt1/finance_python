# -*- coding: utf-8 -*-
"""
Created on Fri Nov 10 19:12:57 2017

@author: sd835979
"""

import numpy as np
import matplotlib as mpt
import matplotlib.pyplot as plt


def plot_scatter_plot():
    y = np.random.standard_normal((1000, 2))
    plt.plot(y[:, 0], y[:, 1], 'ro')
    plt.grid(True)
    plt.xlabel('index')
    plt.ylabel('value')
    plt.title('Scatter Plot')

def plot_colored_scatter_plot():
    y = np.random.standard_normal((1000, 2))
    c = np.random.randint(0, 10, len(y))
    plt.figure(figsize=(7,5))
    plt.scatter(y[:, 0], y[:, 1], c=c, marker='o')
    plt.colorbar()
    plt.grid(True)
    plt.xlabel('index')
    plt.ylabel('value')
    plt.title('Scatter Plot')

def plot_histogram():
    y = np.random.standard_normal((1000, 2))
    plt.hist(y, label=['1st', '2nd'], bins=25)
    plt.grid(True)
    plt.legend(loc=0)
    plt.xlabel('value')
    plt.ylabel('frequency')
    plt.title('Histogram')

#plot_scatter_plot()
#plot_colored_scatter_plot()
#plot_histogram()

