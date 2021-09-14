"""
协变基矢量，是不是某一点上，曲线坐标系到笛卡尔坐标系的变换矩阵？
如果知道某个矢量的极坐标读数，用这个变换矩阵可以找到笛卡尔读数？

需要知道极坐标的参数方程。即笛卡尔x,y如何用r, theta表示。 然后对两个方程求r和theta的偏导数。

三维情况差不多。可以用笛卡尔和球面坐标来表示。

二维就用曲线来表示。一样可以讨论 christoffel symbol


如何设置坐标刻度？
"""
import matplotlib.pyplot as plt
# import numpy as np
from matplotlib.axes import Axes
from sympy import *

EDGE = 6
color = ['w', 'w', 'w', 'w']


def fx(r, theta):
    return r * cos(theta)


def fy(r, theta):
    return r * sin(theta)


fig = plt.figure()  # initializing the figure
# 相当于指定边距，前两个参数指定底边和左边距的百分比，后两个参数指定宽度高度的百分比
rect = [0.1, 0.1, 0.8, 0.8]
ax_cartesian: Axes = fig.add_axes(rect)  # the carthesian axis:
ax_cartesian.set_aspect('equal')
ax_cartesian.grid(True, color='lightblue')
ticks = range(-EDGE, EDGE+1)
ax_cartesian.set_xticks(ticks)
ax_cartesian.set_yticks(ticks)

# ax_carthesian.add_artist(plt.Circle((0.5, 0.5), 5 / 15, color='r', fill=False))
r = 3
theta = pi / 4
x = fx(r, theta)
y = fy(r, theta)
print("x=", x, "y=", y)
# ax_cartesian.scatter([x], [y], s=9)
line1 = [(0, 0), (x, y)]
(line1_xs, line1_ys) = zip(*line1)
# 不能再绘制极坐标之后绘制，会破坏笛卡尔坐标
ax_cartesian.add_line(plt.Line2D(line1_xs, line1_ys))

ax_polar: Axes = fig.add_axes(rect, polar=True, frameon=False)  # the polar axis:
ax_polar.set_yticks(range(0, EDGE+1))
# theta = np.linspace(-np.pi, np.pi, 100)
# ax_polar.plot(theta, 1 - np.sin(3 * theta), color='Tomato', ls='--', lw=1, label='a 3-fold curve')
# ax_polar.plot(theta, 1 + np.cos(theta), color='purple', linewidth=1, ls='-', label='a cardioid')

plt.show()
