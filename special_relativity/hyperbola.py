from sympy import *

c, v, y = symbols('c v gamma')
s = y*Matrix([1, v/c**2])
t = y*Matrix([v, 1])

exp = (y*(1+(v/c**2)**2-v**2-1)).subs(y, 1/sqrt(1-v**2/c**2))
pprint(exp)
