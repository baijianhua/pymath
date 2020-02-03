from sympy import *
from common import plot_equation

x, y = symbols('x y')
eq = Eq(x ** 2 + y ** 2, 36)
plot_equation(eq, (x, -8, 8), (y, -8, 8))

