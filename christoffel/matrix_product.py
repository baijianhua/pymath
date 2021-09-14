from sympy import *

"""
把矩阵解释为局部坐标系的基向量在笛卡尔坐标的读数，乘数向量解释为向量在局部坐标系的读数
把其乘机解释为求局部向量的笛卡尔读数，这个解释真的很漂亮

可是向量乘以矩阵是怎么解释呢？如果能够解释，那就可以更好的解释度量张量。现在这样将度量张量
解释为雅克比矩阵的转置矩阵*雅可比矩阵，还是有点蹩脚。前半部分的解释不够自然。

后半部分是很漂亮的，把局部读数转化为笛卡尔读数。前面也是这个本质，但不巧的是却是用一个向量
乘以基向量的矩阵的转置。

第一个想到度量张量的定义的人，可能就没那么自然了。我想那个人应该有更自然的形式想到这个度量张量。

很怀疑度量张量和力学里面的张量不是一个东西。感觉讲解的出入很大。
"""
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
