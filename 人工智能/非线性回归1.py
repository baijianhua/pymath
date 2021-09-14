from sympy import *
from numpy import *
import sympy as sp
# import numpy as np


def sigmoid(_x):
    return 1/(1+sp.exp(-_x))


def loss(z2_1, z2_2, y_1, y_2):
    return ((z2_1 - y_1)**2 + (z2_2 - y_2)**2)/2

z2_1, z2_2 = symbols("z2_{1} z2_{2}")
a_1, a_2 = symbols("a_1, a_2")
y_1, y_2 = symbols("y_1, y_2")
w2_1, w2_2 = symbols("w2_1, w2_2")

diff(loss(z2_1, z2_2, y_1, y_2), )

