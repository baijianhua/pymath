from sympy import *


c, t, v, x1 = symbols("c t v x'")
a = Symbol("alpha")
eq1 = Eq(c * t, v * t + sqrt(c**2 - v**2))
pprint(eq1)

t1 = solve(eq1, t)
pprint(t1)

# t1 = t1 * sqrt(c ** 2 - v ** 2) / c
# # t1 = factor(t1)
# # t1 = cancel(t1)
# t1 = t1.simplify()
pprint(t1)
# print_latex(Eq(t, t1))

# eq1 = Eq(1, t ** 2 - 2 * v * t * x1 / (c ** 2 - v ** 2))
# t1 = solve(eq1, t)[0]
# t1 = t1 * c / sqrt(c ** 2 - v ** 2)
# t1 = t1.simplify()
# pprint(t1)
