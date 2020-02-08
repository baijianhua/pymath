from sympy import symbols, sin, cos, pi, latex, pprint
from sympy.diffgeom import Manifold, Patch, CoordSystem
from sympy.simplify import simplify

from common import plot_latex

r, theta = symbols('r, theta')
x, y = symbols('x, y')
m = Manifold('M', 2)
# 定义一个patch
patch = Patch('P', m)
# 为这个patch建立坐标系，一个是笛卡尔，一个是极坐标
rect: CoordSystem = CoordSystem('rect', patch)
polar = CoordSystem('polar', patch)
# print(rect in patch.coord_systems)
# 建立两个坐标系之间的转换关系，逆变换是自动的。
# 这个地方，如果笛卡尔是3维，另一个是2维曲面（但是也用u,v，不用极坐标，那会怎么样呢？）
polar.connect_to(rect, [r, theta], [r*cos(theta), r*sin(theta)])
# t = polar.coord_tuple_transform_to(rect, [1, pi])
# 极坐标存在奇点，r = 0时，其他怎么取都是0

t = polar.coord_tuple_transform_to(rect, [0, pi])
print(t)
t = polar.coord_tuple_transform_to(rect, [2, pi/2])
print(t)
t = rect.coord_tuple_transform_to(polar, [0, 2])
print(t)

# 雅克比矩阵。极坐标到笛卡尔坐标系的变换矩阵函数，在每个点，是可以求出一个具体的矩阵的
# 但整体来说是一个函数。
m = polar.jacobian(rect, [r, theta])
print(m)
plot_latex(latex(m))
# 笛卡尔坐标系到笛卡尔坐标系的雅克比矩阵是单位矩阵
m = rect.jacobian(rect, [x, y])
# plot_latex(latex(m))


p = rect.point([3, 2])
# base_vector返回一个向量场。给定一个点，会返回一个向量？
# v_x = rect.base_vector(0)
# v_y = rect.base_vector(1)
# pprint(v_x(p), v_y(p))

# 返回标量场。标量场的意思是取一个点，返回一个标量值。x y轴可以视为两个天然的标量场，但应该开可以返回其他标量场
x_scalar_field = rect.coord_function(0)

# 返回横坐标
print(x_scalar_field(p))

# base_oneform返回的又是什么？
# pprint(rect.base_oneform(0))
