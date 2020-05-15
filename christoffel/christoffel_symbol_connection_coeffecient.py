import sympy as sym
from sympy import *


a, b, x, y, f_x, f_y, r, theta = symbols('a, b, x, y, f_x, f_y, r, theta')
e_r, e_theta, e_r_x, e_r_y, e_theta_x, e_theta_y = \
    symbols('e_r, e_\\theta, e_{r_x},e_{r_y}, e_{\\theta_x}, e_{\\theta_y}')


fx = r * cos(theta)
fy = r * sin(theta)

erx = diff(fx, r)
ery = diff(fy, r)
# print_latex(erx)
# print_latex(ery)

etx = diff(fx, theta)
ety = diff(fy, theta)

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

