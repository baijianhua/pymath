from sympy import *

y, c, v = symbols('gamma, c, v')
x, t, x1, t1 = symbols('x, t, x\', t\'')
tensor = Matrix([[1, v/c**2], [v, 1]])
v = Matrix([x, t])
v1 = Matrix([x1, t1])

eq = Eq(v, Mul(y, tensor, v1, evaluated=False))
print_latex(eq)

