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
    """将fx,fy对theta偏微分，可知在一个特定的r,theta点，当theta发生变动时，x,y各自怎样变化"""
    e_theta_x = diff(fx, theta)
    e_theta_y = diff(fy, theta)
    # pprint(e_theta_x)
    # pprint(e_theta_y)
    """将fx,fy对r偏微分，可知在一个特定的r,theta点，当r发生变动时，x,y各自怎样变化,
    代入r,theta,可得到变化的方向和强度（用与r,theta点之间的线段表示）"""
    e_r_x = diff(fx, r)
    e_r_y = diff(fy, r)

    # pprint(e_r_x)
    # pprint(e_r_y)

    def fxy(a, b):
        return fx.subs({r: a, theta: b}), fy.subs({r: a, theta: b})

    def substitution_exp_and_draw(exp1: Function, exp2: Function, a, b, color='black', linewidth=1):
        """
        注意，以sx,sy为起点，终点却不是ex,ey,erx,ery,还要做一个坐标转换。因为那些值是以sx,sy为原点算出来的。
        直接计算出来的ex,ey并不是向量在以0,0为原点的笛卡尔坐标系的终点，而是以sx,sy为原点的变化幅度。所以真正
        想要映射到0,0为原点的笛卡尔坐标系，需要加上sx,sy。
        :param b:
        :param a:
        :param exp2:
        :param exp1:
        :param color:
        :param color:
        """
        (sx, sy) = fxy(a, b)
        ex = sx + exp1.subs({r: a, theta: b})
        ey = sy + exp2.subs({r: a, theta: b})
        print('---------------------')
        pprint(exp1)
        pprint(exp2)
        print("r=", a, "theta=", b)
        print("x0=", sx, "y0=", sy, "val=", sx.evalf(), sy.evalf())
        print("x1=", ex, "y1=", ey, "val=", ex.evalf(), ey.evalf())

        draw_vector(ax_cartesian, (sx, sy), (ex, ey), color, linewidth)

    def draw_e(a, b, color='red'):
        substitution_exp_and_draw(e_theta_x, e_theta_y, a, b, color)
        substitution_exp_and_draw(e_r_x, e_r_y, a, b, color)

    # pprint(sin(pi/4))
    # pprint(cos(pi/4))
    # draw_e(3, pi / 6)
    draw_e(3, 0)
    # draw_e(1, pi / 4)
    # draw_e(5, pi / 2)
    # draw_e(4, 0)

    """
    接下来就到了联络系数，也就是Christoffel Symbol了，却有点晕乎乎的，到底是谁针对谁的变化？
    当theta移动，原来的两个向量都会变化。
    
    原来的基向量e_theta，是由r,theta和 e_theta_x = diff(fx,theta) 
                                     e_theta_y = diff(fy,theta)构成的。

    那么，当theta变化的时候，e_theta的变化就是 e_theta_x_theta = diff(e_theta_x,theta), 
                                            e_theta_y_theta = diff(e_theta_y,theta),

    同样，当r变化，也会导致e_theta的变化，其变化为                                  
                                            e_theta_x_r = diff(e_theta_x,r),
                                            e_theta_x_r = diff(e_theta_y,r),          
    """
    e_theta_x_theta = diff(e_theta_x, theta)
    e_theta_y_theta = diff(e_theta_y, theta)
    e_theta_x_r = diff(e_theta_x, r)
    e_theta_y_r = diff(e_theta_y, r)

    e_r_x_theta = diff(e_r_x, theta)
    e_r_y_theta = diff(e_r_y, theta)
    e_r_x_r = diff(e_r_x, r)
    e_r_y_r = diff(e_r_y, r)

    def draw_de(a, b, color="green"):
        substitution_exp_and_draw(e_theta_x_theta, e_theta_y_theta, a, b, 'black', 2)
        substitution_exp_and_draw(e_theta_x_r, e_theta_y_r, a, b, 'black', 2)
        substitution_exp_and_draw(e_r_x_theta, e_r_y_theta, a, b, 'blue', 2)
        substitution_exp_and_draw(e_r_x_r, e_r_y_r, a, b, 'blue', 2)

    draw_de(3, 0)
    draw_e(1, EDGE/360)


def draw_vector(ax: Axes, start_point: MsPoint, end_point: MsPoint, color='red', linewidth=1):
    line1 = [start_point, end_point]
    # zip是拿来做什么的？将两个点生成序列？
    (line1_xs, line1_ys) = zip(*line1)
    # 不能再绘制极坐标之后绘制，会破坏笛卡尔坐标
    ax.add_line(plt.Line2D(line1_xs, line1_ys, color=color, linewidth=linewidth))


draw_cartesian_polar()
plt.show()
