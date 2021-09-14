from sympy import *


def square(num):
    return num * num


y = symbols('y', positive=True)
x = Symbol('x', nonegative=True)
eq = Eq(square(x) + square(y), 3)
print_latex(solveset(eq, x, domain=S.Reals))
