from sympy import *
from common1 import plot_latex

x, y, z, theta, r = symbols(r'x y z \theta r')
fx = r * sin(theta)
fy = r * cos(theta)
# r2 = latex(diff(expr1, x, evaluate=False))
r3 = diff(fx, theta, evaluate=False)
pprint(r3)
plot_latex(latex(r3))

