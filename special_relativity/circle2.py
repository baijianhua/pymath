from sympy import *

c, t, v, x, gamma, t1, x1 = symbols("c t v x gamma t' x'")
a = Symbol("alpha")

eq1 = Eq((c*t1)**2, (c * t)**2 + (v*t)**2 - 2 * c * t * v * t * x /(c*t) )

pprint(eq1)
t_exp = solve(eq1, t)[1]
t_exp = t_exp.subs(x, (x1+v*t1)/sqrt(1-(v/c)**2))
# t1 = t1.subs(gamma, sqrt(1-v**2/c**2))
t_exp = t_exp.simplify()
pprint(t_exp)
print_latex(Eq(t, t_exp))
