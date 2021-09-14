from sympy import *
from common1 import plot_latex, plot_equation

x, y = symbols('x y')
eq = Eq(x**2 + y**2, 9)
plot_equation(eq)
