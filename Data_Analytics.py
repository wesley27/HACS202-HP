#!/usr/bin/env python

import pandas as pd
import numpy as np
import matplotlib.pyplot

data = pd.read_csv("/Users/CAM_CAM_1/Downloads/????")
#print(data.columns)

def function1():
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

def function3():
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
