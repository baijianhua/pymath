from sympy import *
from numpy import *
# import numpy as np


def Sigmoid(x):
    a = 1.0 / (1.0 + np.exp(-x))
    return a


x = symbols("x")
w11, w12 = symbols("w1_{1} w1_{2}")
b11, b12 = symbols("b1_{1} b1_{2}")
W1 = Matrix([w11, w12])
B1 = Matrix([b11, b12])

# print_latex(W1)

Z1 = x * W1 + B1

pprint(Z1)

print_latex(Z1)
# A1 = Sigmoid(Z1)
# print(x)
