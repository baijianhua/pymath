from sympy import *

r, theta = symbols('r, theta')
# polar to cartesian
fx = r * cos(theta)
fy = r * sin(theta)

# base vector
erx = diff(fx, r)
ery = diff(fy, r)
etx = diff(fx, theta)
ety = diff(fy, theta)

# base vector changes.
erxr = diff(erx, r)
eryr = diff(ery, r)
etxr = diff(etx, r)
etyr = diff(ety, r)

erxt = diff(erx, theta)
eryt = diff(ery, theta)
etxt = diff(etx, theta)
etyt = diff(ety, theta)

print_latex(erxr)
print_latex(eryr)
print_latex(etxr)
print_latex(etyr)

print_latex(erxt)
print_latex(eryt)
print_latex(etxt)
print_latex(etyt)

# christoffel symbol
print("resolve equations=============")
a, b = symbols('Gamma^r_rr, Gamma^theta_rr')
eq1 = a * erx + b * etx - erxr
eq2 = a * ery + b * ety - eryr
print_latex(solve([eq1, eq2], [a, b]))

a = Symbol('\\Gamma^r_{\\theta r}')
b = Symbol('\\Gamma^\\theta_{\\theta r}')
eq1 = a * erx + b * etx - etxr
eq2 = a * ery + b * ety - etyr
print_latex(solve([eq1, eq2], [a, b]))

a = Symbol('\\Gamma^r_{r \\theta}')
b = Symbol('\\Gamma^\\theta_{r \\theta}')
eq1 = a * erx + b * etx - erxt
eq2 = a * ery + b * ety - eryt
print_latex(solve([eq1, eq2], [a, b]))

a = Symbol('\\Gamma^r_{\\theta \\theta}')
b = Symbol('\\Gamma^\\theta_{\\theta \\theta}')
eq1 = a * erx + b * etx - etxt
eq2 = a * ery + b * ety - etyt
print_latex(solve([eq1, eq2], [a, b]))
