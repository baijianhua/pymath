import matplotlib.pyplot as plt
# from matplotlib import Axes
from matplotlib.axes import Axes
import numpy as np

from common import plot_equation

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
ticks = range(-1, 20)
ax_cartesian.set_yticks(ticks)

xx, yy = np.linspace(-5, 5), np.linspace(-1, 20)
x, y = np.meshgrid(xx, yy)
ax_cartesian.contour(x, y, x**2 - y, 0)

# 如何定义曲线各点的坐标，以及他们的雅克比矩阵？并如何绘制？
# 这样做应该是可以成功的，但很难验证，因为别人很少有做这样运算

plt.show()
