import sympy as sym
from sympy import *


a, b, x, y, f_x, f_y, r, theta = symbols('a, b, x, y, f_x, f_y, r, theta')
e_r, e_theta, e_r_x, e_r_y, e_theta_x, e_theta_y = \
    symbols('e_r, e_\\theta, e_{r_x},e_{r_y}, e_{\\theta_x}, e_{\\theta_y}')


fx = r * cos(theta)
fy = r * sin(theta)

local_bases = Matrix([[e_r, e_theta]])
local_bases_xy = Matrix([
    [e_r_x, e_theta_x],
    [e_r_y, e_theta_y]
])
local_vector = Matrix([a, b])
cartesian_vector = MatMul(local_bases, local_vector, evaluated=false)
print_latex(cartesian_vector)

# fx_exp = Eq(f_x, fx)
# fy_exp = Eq(f_y, fy)
# print("exp of et_x")
# et_x = Derivative(fx, theta)
# print_latex(et_x)
# et_y = diff(fy, theta)
ferx = Eq(e_r_x, diff(fx, r))
fery = Eq(e_r_y, diff(fy, r))

# print_latex(et_x)
# print_latex(et_y)
print_latex(e_r_x)
print_latex(e_r_y)

# d_etx = diff(et_x, theta) + diff(et_x, r)
# d_ety = diff(et_y, theta) + diff(et_y, r)
# d_erx = diff(e_rx, theta)+diff(e_ry, r)
# d_ery = diff(e_rx, theta)+diff(e_ry, r)
# print_latex(d_etx)
# print_latex(d_ety)
# print_latex(d_erx)
# print_latex(d_ery)

"""
我想联络系数、克氏符这个东西，最主要的作用，应该就是坐标平移
或者说是为了比较单位基向量（方向或模长）在不断变化的坐标系中不同位置的向量

那么怎么叫做平移呢？如果一个向量可以表示成a*ex,b*ey
不管ex,ey这个基向量怎样变化，也就是说，在ex0,ey0这一点，v的形式是a*ex0,b*ey0
在ex1,ey1这一点，v的形式仍然是a*ex1,b*ey1, 这个向量就是没有变化。

这里有一点费解，就是e*ex, b*ey, 但要习惯这种方法，坐标系就是这么用的不要习惯于用x,y来表达问题
而是要始终把n维向量理解成任意n个尾部相连的线性不相关的向量的倍数。

这里ex = fx(x,y),ey=fy(x,y), 在不同的点(x,y)处，会有不同的基向量，不同的局部坐标系。

任意位置的两个向量，如果能够用同一基向量组表示，那么他们之间就可以比较。进行加减等运算。不要
去想如果坐标系是点状的东西，怎么容纳有长度的向量呢？不是在不同位置度量不同吗？错！始终要
明白向量是个点，只在点域内有意义，不存在延伸到另一个度量不同的邻域的问题，要么在这个域，要么
在下个域，向量不会同时在两个域！！！！！！！！！

那么怎么才能找到ex0,ey0与ex1,ey1之间的转换关系呢？积分是一个手段。或许奇怪，如果向量随x,y变化
的函数已知，那直接把一点处的基向量换算成另一点处基向量不就行了吗？不就可以验证不变性了吗？

确实是。但那样就没有利用微积分中的一些好方法了。比如导数、极值、积分这些东西。有点运算可能还是很复杂
的。不借助积分可能让人摸不着头绪。
"""
