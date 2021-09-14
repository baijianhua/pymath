from sympy import diff, Matrix
from sympy import symbols
from sympy import exp
from sympy import print_latex


def sigmoid(_x):
    return 1/(1+exp(-_x))


def fz2(w2_1, w2_2, b2, a_1, a_2):
    return w2_1*a_1 + w2_2*a_2 + b2


z2_1, z2_2 = symbols("z2_{1} z2_{2}")
a_1, a_2 = symbols("a_1, a_2")
y_1, y_2 = symbols("y_1, y_2")
w2_1, w2_2, b2 = symbols("w2_{1}, w2_{2}, b2")

print_latex(fz2)
d = diff(fz2(w2_1, w2_2, b2, a_1, a_2), a_1)
print_latex(d)

Z2 = Matrix([z2_1, z2_2])
Y = Matrix([y_1, y_2])
W2 = Matrix([w2_1, w2_2])
dZ2 = Z2 - Y
print_latex(dZ2.T.dot(W2))


