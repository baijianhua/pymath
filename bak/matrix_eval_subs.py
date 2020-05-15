from sympy import *

r, theta, a, b = symbols('r, theta, a, b')
fx = r * sin(theta)
fy = r * cos(theta)

er_x = diff(fx, r)
er_y = diff(fy, r)
et_x = diff(fx, theta)
et_y = diff(fy, theta)

m = Matrix([
    [er_x, et_x],
    [et_x, et_y]
])
v = Matrix([a, b])
cv = MatMul(m, v)
print_latex(cv.subs({r: 3, theta: pi / 6, a: 3, b: 4}).evalf())
