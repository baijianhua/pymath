"""
协变基矢量，是不是某一点上，曲线坐标系到笛卡尔坐标系的变换矩阵？
如果知道某个矢量的极坐标读数，用这个变换矩阵可以找到笛卡尔读数？

需要知道极坐标的参数方程。即笛卡尔x,y如何用r, theta表示。 然后对两个方程求r和theta的偏导数。


"""
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.axes import Axes

color = ['w', 'w', 'w', 'w']
fig = plt.figure()  # initializing the figure
# 相当于指定边距，前两个参数指定底边和左边距的百分比，后两个参数指定宽度高度的百分比
rect = [0.1, 0.1, 0.8, 0.8]
ax_carthesian: Axes = fig.add_axes(rect)  # the carthesian axis:
ax_carthesian.set_aspect('equal')
ax_carthesian.grid(True, color='lightblue')


# ax_carthesian.add_artist(plt.Circle((0.5, 0.5), 5 / 15, color='r', fill=False))
# ax_carthesian.add_artist(plt.Circle((0.5, 0.5), 4.5 / 15, color='g', fill=False))
# ax_carthesian.add_artist(plt.Circle((0.5, 0.5), 5.445 / 15, color='b', fill=False))

theta = np.linspace(-np.pi, np.pi, 100)
ax_polar: Axes = fig.add_axes(rect, polar=True, frameon=False)  # the polar axis:


# ax_polar.plot(theta, 1 - np.sin(3 * theta), color='Tomato', ls='--', lw=1, label='a 3-fold curve')
# ax_polar.plot(theta, 1 + np.cos(theta), color='purple', linewidth=1, ls='-', label='a cardioid')

plt.show()
