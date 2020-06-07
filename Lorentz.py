from sympy import *

x, y, z, t, c = symbols("x,y,z,t,c")
x1, y1, z1, t1 = symbols("x',y',z',t'")
gamma, v = symbols('gamma, v')
eq1 = Eq(x, gamma * (x1 + v * t1))
eq2 = Eq(x1, gamma * (x - v * t))

# t1 的表达式，用x,v,x1表示
# x1 的表达式，用x,v,t表示
t1_exp = solve(eq1, t1)[0]
x1_exp = solve(eq2, x1)[0]
# x 的表达式，用x1,v,t1表示
x_exp = solve(eq1, x)[0]
# 将t1用x1表示
t1_exp_subs = t1_exp.subs(x1, eq2.rhs).simplify()
x_x1_exp = (x_exp * x1_exp).subs({x: c * t, x1: c * t1})
print("x*x1=")
print_latex(x_x1_exp)
eq3 = Eq(c * t * c * t1, x_x1_exp)
gamma_exp = solve(eq3, gamma)[0].simplify()
print_latex(gamma_exp)
pprint(gamma_exp)
