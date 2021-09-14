import matplotlib
from matplotlib.figure import Figure
from mpl_toolkits.mplot3d import Axes3D
from sympy import *
from sympy.diffgeom import *
import matplotlib.pyplot as plt
import numpy as np

from common1 import plot_latex

R = 10
GRID = 10


def draw_shape():
    fig: Figure = plt.figure()  # figsize=(200, 200)
    ax: Axes3D = fig.add_subplot(111, projection='3d')
    # 经度
    u = np.linspace(0, 2 * np.pi, GRID * 2 + 1)
    # 纬度
    v = np.linspace(0, np.pi, GRID)

    x = R * np.outer(np.cos(u), np.sin(v))
    y = R * np.outer(np.sin(u), np.sin(v))
    z = R * np.outer(np.ones(np.size(u)), np.cos(v))
    ax.plot_wireframe(x, y, z, color='lightblue')
    return ax


def coords():
    rho = R
    u, v = symbols('u, v')
    x, y, z = symbols('x, y, z')
    m = Manifold('M', 3)
    # 定义一个patch
    patch = Patch('P', m)
    # 为这个patch建立坐标系，一个是笛卡尔，一个是极坐标
    rect: CoordSystem = CoordSystem('rect', patch)
    polar: CoordSystem = CoordSystem('spherical', patch)
    polar.connect_to(rect,
                     [u, v],
                     [rho * sin(u) * cos(v), rho * sin(u) * sin(v), rho * cos(u)])

    # jacobian
    j = polar.jacobian(rect, [u, v])
    # print("jocobian=", j)
    print("jacobian latex=", latex(j))
    # plot_latex(latex(j))
    m = j.T @ j
    # print("metrics tensor-----------------------", m)
    # pprint(m)
    print("metrics tensor latex=", latex(m))
    # plot_latex((latex(j)))
    return polar, rect


def plot_uv(polar, u, v, color="green"):
    pt = polar.coord_tuple_transform_to(rect, [u, v])
    pt1: Point3D = Point3D(pt)
    print(pt1)
    # line = Line3D(Point3D(0, 0, 0), Point3D(5, 5, 5))
    # ax.add_line(line)
    ax.plot([0, pt1.x], [0, pt1.y], [0, pt1.z], color=color)
    print(pt)


ax = draw_shape()
polar, rect = coords()

# 纵向的两个轴，给定的坐标其实是球面的，只是绘制从球心开始绘制而已。
# u是纬度值， v是经度。
# 当纬度是0或者是pi, 经度任取。分别是南极和北极
plot_uv(polar, 0, 0, color='r')
plot_uv(polar, pi, 0, color='black')

# 横向的四个球轴，位于赤道
plot_uv(polar, np.pi / 2, 0, color='r')
plot_uv(polar, np.pi / 2, pi / 2, color="yellow")
plot_uv(polar, np.pi / 2, pi, color="green")
plot_uv(polar, np.pi / 2, 3 * pi / 2, color="blue")

# 在上半球找一个点
plot_uv(polar, np.pi / 4, pi, color="blue")

"""接下来就是利用christoffel symbol计算测地线了"""
# 怎样才能在3d网格上绘制活动标架呢？并最终绘制测地线（两个点之间的大圆）
# 选取球面上的任意一点，计算这一点的变换矩阵，并绘制局部笛卡尔坐标系
# 如果一个曲面是不规则的，那要如何计算雅可比矩阵，Christoffel Symbol呢？

plt.show()
