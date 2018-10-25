#!/usr/bin/env python

import pandas as pd
import numpy as np
import matplotlib.pyplot

data = pd.read_csv("/Users/CAM_CAM_1/Downloads/????")
#print(data.columns)

def histogram():
    """
    The python functions below will work to create a histogram.
    """
    plt.style.use('seaborn')
    fig = plt.figure()
    plt.hist(data[""])
    plt.title("")
    plt.xlabel("")
    plt.ylabel("")
    plt.show()

def scatter():
    """
    The python functions below will work to create a scatter plot.
    """
    plt.style.use('seaborn')
    fig = plt.figure()
    plt.scatter(data[""], data[""], marker='.')
    plt.title("")
    plt.xlabel("")
    plt.ylabel("")
    plt.show()

def scatter_regression():
    """
    The python functions below will work to create a scatter plot with a
    regresison line.
    """
    plt.style.use('seaborn')
    fig = plt.figure()
    plt.scatter(data[""], data[""], marker='.')
    m, b = np.polyfit(data[""], data[""], 1)
    x = np.linspace(10,1000, 10000)
    plt.plot(x,m*x+b, linestyle='--')
    plt.title("")
    plt.xlabel("")
    plt.ylabel("")
    plt.show()
