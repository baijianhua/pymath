from sympy import *

x = symbols('x')
y = symbols('y')
eq1 = x + y - 6
eq2 = x - y - 2
print(solve([eq1, eq2], [x, y]))
