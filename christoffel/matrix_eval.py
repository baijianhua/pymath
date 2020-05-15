from sympy import *

r, theta, a, b = symbols('r, theta, a, b')
fx = r * sin(theta)
fy = r * cos(theta)

er_x = diff(fx, r)
er_y = diff(fy, r)
et_x = diff(fx, theta)
et_y = diff(fy, theta)

# print_latex(er_x.subs({r: 3, theta: pi/6}).evalf())

m = Matrix([
    [er_x, et_x],
    [et_x, et_y]
])

v = Matrix([a, b])
cv = MatMul(m, v)

"""
如果不调用evalf(),就会是分数形式, 如果不执行doit(), 那就会保留矩阵乘法的形式
"""
print_latex(cv.subs({r: 3, theta: pi/6, a: 3, b: 2}).doit().evalf())
