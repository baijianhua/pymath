from sympy import *
from common import plot_latex

x, y, z = symbols('x_{1}^2 y z1')
expr1 = exp(x*y*z)
# r2 = latex(diff(expr1, x, evaluate=False))
r3 = latex(diff((x, y), x, evaluate=False))
plot_latex(r3)

