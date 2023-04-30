# Import libraries
import numpy as np
from scipy import optimize
import math

# First we define the functions, YOU SHOULD IMPLEMENT THESE
def f (x, y) :
    return np.exp(x-y**2+x*y)*(-1)

def g (x, y) :
    return math.cosh(y)+x-2

# Next their derivatives, YOU SHOULD IMPLEMENT THESE
def dfdx (x, y) :
    return np.exp(x-y**2+x*y)*(1+y)*-1

def dfdy (x, y) :
    return np.exp(x-y**2+x*y)*(-2*y+x)

def dgdx (x, y) :
    return 1
def dgdy (x, y) :
    return math.sinh(y)

# Use the definition of DL from previously.
def DL (xyλ) :
    [x, y, λ] = xyλ
    return np.array([
            dfdx(x, y) - λ * dgdx(x, y),
            dfdy(x, y) - λ * dgdy(x, y),
            - g(x, y)
        ])

# To score on this question, the code above should set
# the variables x, y, λ, to the values which solve the
# Langrange multiplier problem.

# I.e. use the optimize.root method, as you did previously.

x, y, λ = optimize.root(DL, [0, 0, 1]).x

print("x = %g" % x)
print("y = %g" % y)
print("λ = %g" % λ)
print("f(x, y) = %g" % f(x, y))
