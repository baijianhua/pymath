from sympy import *
from common import plot_latex

x, y = symbols('x y')
f = Function('f1')
g = Function('g')(x)

plot_latex(latex(f(x, y).diff(x)))
