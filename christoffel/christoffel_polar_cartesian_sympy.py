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
from typing import Tuple

MsPoint = Tuple[float, float]

a, b = symbols('a, b')


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
    EDGE = 8
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
    # draw_vector(ax_cartesian, (0, 0), Point2D(3, 3), color='blue')

    ax_polar: Axes = fig.add_axes(layout, polar=True, frameon=False)  # the polar axis:
    ax_polar.set_yticks(range(0, EDGE + 1))

    r, theta = symbols('r, theta')

    """这两个函数，用来确定r和theta与x,y之间的对应关系，给定一对儿r,theta，可以确定一对x,y"""
    fx = r * cos(theta)
    fy = r * sin(theta)

    def subs(exp1, exp2, a, b):
        return exp1.subs({r: a, theta: b}), exp2.subs({r: a, theta: b})

    def draw_expr(a, b, exp1, exp2, color='red', linewidth=2):
        x0, y0 = subs(fx, fy, a, b)
        x1, y1 = subs(exp1, exp2, a, b)
        draw_vector(ax_cartesian, (x0, y0), (x0 + x1, y0 + y1), color, linewidth)

    def draw_vector_from_x0_y0(x1, y1, color='red', linewidth=2):
        draw_vector(ax_cartesian, (x0, y0), (x0 + x1, y0 + y1), color, linewidth)

    r0, t0 = (3, pi / 6)
    x0, y0 = subs(fx, fy, r0, t0)
    """将fx,fy对r偏微分，可知在一个特定的r,theta点，当r发生变动时，x,y各自怎样变化,
        代入r,theta,可得到变化的方向和强度（用与r,theta点之间的线段表示）"""
    e_rx = diff(fx, r)
    e_ry = diff(fy, r)
    """将fx,fy对theta偏微分，可知在一个特定的r,theta点，当theta发生变动时，x,y各自怎样变化"""
    e_tx = diff(fx, theta)
    e_ty = diff(fy, theta)
    """
    局部坐标系的两个基向量
    """
    draw_expr(r0, t0, e_rx, e_ry)
    draw_expr(r0, t0, e_tx, e_ty)
    """在局部坐标系绘制一个局部向量"""
    local_coord = Matrix([[e_rx, e_tx],
                          [e_ry, e_ty]
                          ])
    local_vector_exp = MatMul(local_coord, Matrix([a, b]))
    pprint(local_vector_exp.doit())
    local_vector = local_vector_exp.subs({r: r0, theta: t0, a: 2, b: 1}).doit().evalf()

    x1 = local_vector[0]
    y1 = local_vector[1]
    draw_vector_from_x0_y0(x1, y1)

    """
    当r变动时，两个基向量会怎样变化？    
    """
    erx_r = diff(e_rx, r)
    ery_r = diff(e_ry, r)
    draw_expr(r0, t0, erx_r, ery_r, color='green')
    etx_r = diff(e_tx, r)
    ety_r = diff(e_ty, r)
    draw_expr(r0, t0, etx_r, ety_r, color='green')

    erx_t = diff(e_rx, theta)
    ery_t = diff(e_ry, theta)
    etx_t = diff(e_tx, theta)
    ety_t = diff(e_ty, theta)
    # draw_exp(3, pi / 6, erx_t, ery_t, 'green')
    # draw_exp(3, pi / 6, etx_t, ety_t, 'green')

    # der =
    # det =


def draw_vector(ax: Axes, start_point: MsPoint, end_point: MsPoint, color='red', linewidth=1):
    line1 = [start_point, end_point]
    # zip是拿来做什么的？将两个点生成序列？
    (line1_xs, line1_ys) = zip(*line1)
    # 不能再绘制极坐标之后绘制，会破坏笛卡尔坐标
    ax.add_line(plt.Line2D(line1_xs, line1_ys, color=color, linewidth=linewidth))


draw_cartesian_polar()
plt.show()
