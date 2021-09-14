from sympy import *
from numpy import *

import sympy as sp
# import numpy as np

def sigmoid(_x):
    # return 1/(1+sp.exp(-_x))
    return _x ** 2


w21, w22 = symbols("w2_{1} w2_{2}")
dz2_1, dz2_2 = symbols("dz2_1 dz2_2")
dz2_1, dz2_2 = symbols("dz2_1 dz2_2")

W2 = Matrix([w21, w22])
dZ2 = Matrix([dz2_1, dz2_2])
print_latex(dZ2.dot(W2))

