from sympy import *
from common import plot_equation

x, y = symbols('x y')
eq = Eq(2*x+3 - y, 0)
plot_equation(eq, (x, -8, 8), (y, -8, 8))
# plot(2*x+3)
