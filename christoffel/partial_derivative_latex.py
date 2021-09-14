from sympy import *

x, y = symbols('x, y')
r, theta = symbols("r, theta")

exp = limit(sin(x)/x, x, 0, evaluated=false)
print_latex(exp)

fx = r * sin(theta)
print_latex(fx.diff(r))
print_latex(fx.diff(r, 1))

m, n, a, b = symbols('m n a b')
expr = (a*x + b)**m
print_latex(expr.diff((x, n)))

# print_latex(diff(x, r))
# fy = Eq(y, r * cos(theta))


erx = "\\frac{\partial fx(r,\\theta)}{\partial r}"
ery = "\\frac{\partial fy(r,\\theta)}{\partial r}"
etx = "\\frac{\partial fy(r,\\theta)}{\partial \\theta}"
ety = "\\frac{\partial fy(r,\\theta)}{\partial \\theta}"

erx_r = "\\frac{\partial^2 fx(r,\\theta)}{\partial r \partial r}"
ery_r = "\\frac{\partial^2 fy(r,\\theta)}{\partial r \partial r}"

# er = Matrix([erx, ery])

print_latex(erx)
print_latex(ery)
print_latex(etx)
print_latex(ety)
print_latex(erx_r)
print_latex(ery_r)
# print_latex(diff(x, r))
