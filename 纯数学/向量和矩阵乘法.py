# https://blog.csdn.net/liuxiang3/article/details/114921870

from sympy import *

x1, y1, x2, y2 = symbols("x1 y1 x2 y2")
u = Matrix([x1, y1])
v = Matrix([x2, y2])
print_latex(u.T.multiply(v))
print_latex(u.T * v)
print_latex(u.dot(v))

print("cross")
u1 = Matrix([x1, y1, 0])
v1 = Matrix([x2, y2, 0])
print_latex(u1.cross(v1))

a, b, c, d, e, f, g, h = symbols("a:h")
X = Matrix(2, 2, [a, b, c, d])
Y = Matrix(2, 2, [e, f, g, h])
print_latex(X)
print_latex(Y)
print_latex(X * Y)
print_latex(X.multiply(Y))
# print_latex(X.dot(Y))
print_latex(X.multiply_elementwise(Y))

a11, a12, a21, a22, a31, a32, b1, b2 = symbols("a11 a12 a21 a22 a31 a32 b1 b2")
X = Matrix(3, 2, [a11, a12, a21, a22, a31, a32])
Y = Matrix(2, 1, [b1, b2])
print_latex(X)
print_latex(Y)
print_latex(X*Y)


dz1, dz2, dz3 = symbols("dz1 dz2 dz3")
w21, w22 = symbols("w2_{1} w2_{2}")
dZ = Matrix(3, 1, [dz1, dz2, dz3])
W = Matrix(1, 2, [w21, w22])
print_latex(dZ)
print_latex(W)
print_latex(dZ*W)
