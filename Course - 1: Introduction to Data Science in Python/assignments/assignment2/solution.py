import pandas as pd
import numpy as np
import scipy
import math


# First we define the functions,
def f (x, y) :
    return np.exp(-(2*x*x + y*y - x*y) / 2)

def g (x, y) :
    return x*x + 3*(y+1)**2 - 1

# Next their derivatives,
def dfdx (x, y) :
    return np.exp(-(2*x*x + y*y - x*y) / 2) * (2*x - y)