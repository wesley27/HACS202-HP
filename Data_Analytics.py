#!/usr/bin/env python

import pandas as pd
import numpy as np
import matplotlib.pyplot

data = pd.read_csv("/Users/CAM_CAM_1/Downloads/comicmovies.csv")
#print(data.columns)

def function1():
    """
    The python functions below will work to create a histogram of the Review
    column in the day.csv data set that was imported.
    """
    plt.style.use('seaborn')
    fig = plt.figure()
    plt.hist(data["Review"])
    plt.title("Comic Movie Review Distribution")
    plt.xlabel("Rating of Reviews")
    plt.ylabel("Number of Reviews")
    plt.show()
    
