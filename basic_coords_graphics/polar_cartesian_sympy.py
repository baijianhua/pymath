"""
协变基矢量，是不是某一点上，曲线坐标系到笛卡尔坐标系的变换矩阵？
如果知道某个矢量的极坐标读数，用这个变换矩阵可以找到笛卡尔读数？

需要知道极坐标的参数方程。即笛卡尔x,y如何用r, theta表示。 然后对两个方程求r和theta的偏导数。

三维情况差不多。可以用笛卡尔和球面坐标来表示。

二维就用曲线来表示。一样可以讨论 christoffel symbol


如何设置坐标刻度？
"""
import matplotlib.pyplot as plt
from matplotlib.axes import Axes
from sympy import *
from sympy.diffgeom import *


def define_coord_sys():
    """定义Manifold, Patch, CoordSystem"""
    r, theta = symbols('r, theta')
    x, y = symbols('x, y')
    m = Manifold('M', 2)
    # 定义一个patch
    patch = Patch('P', m)
    # 为这个patch建立坐标系，一个是笛卡尔，一个是极坐标
    rect: CoordSystem = CoordSystem('rect', patch)
    polar = CoordSystem('polar', patch)
    polar.connect_to(rect, [r, theta], [r * cos(theta), r * sin(theta)])
    # 极坐标存在奇点，r = 0时，其他怎么取都是0
    # t = polar.coord_tuple_transform_to(rect, [0, pi])
    # 想要理解christoffel符号的意义，推导测地线方程。最后推导广义相对论的运动方程。
    # 现在的困难是必须要脱离图形了。因为matplotlib对三维支持很不好。


def draw_cartesian_polar():
    """绘制笛卡尔和极坐标系"""
    EDGE = 6
    # color = ['w', 'w', 'w', 'w']
    fig = plt.figure()  # initializing the figure
    # 相当于指定边距，前两个参数指定底边和左边距的百分比，后两个参数指定宽度高度的百分比
    layout = [0.1, 0.1, 0.8, 0.8]
    ax_cartesian: Axes = fig.add_axes(layout)  # the carthesian axis:
    ax_cartesian.set_aspect('equal')
    ax_cartesian.grid(True, color='lightblue')
    ticks = range(-EDGE, EDGE + 1)
    ax_cartesian.set_xticks(ticks)
    ax_cartesian.set_yticks(ticks)
    line1 = [(0, 0), (2, 2)]
    # zip是拿来做什么的？将两个点生成序列？
    (line1_xs, line1_ys) = zip(*line1)
    # 不能再绘制极坐标之后绘制，会破坏笛卡尔坐标
    ax_cartesian.add_line(plt.Line2D(line1_xs, line1_ys))

    ax_polar: Axes = fig.add_axes(layout, polar=True, frameon=False)  # the polar axis:
    ax_polar.set_yticks(range(0, EDGE + 1))

    plt.show()


define_coord_sys()
draw_cartesian_polar()
