from sympy import *


def pow2(x):
    return x * x


c, t, v, x = symbols("c t v x")
a = Symbol("alpha")
eq1 = Eq(c**2 - v**2, (c * t)**2 + v**2 - 2 * c * t * v * cos(a))
eq1 = eq1.subs(cos(a), (v+x)/c*t)
pprint(eq1)
t1 = solve(eq1, t)[0]
t1 = t1*c/sqrt(c**2-v**2)
# t1 = factor(t1)
# t1 = cancel(t1)
t1 = t1.simplify()
pprint(t1)
print_latex(Eq(t, t1))
