"""
用方程的形式绘制球
https://stackoverflow.com/questions/4680525/plotting-implicit-equations-in-3d

还是没能完全做到，不过有点那个意思。
"""

import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D


def set_axes_radius(ax, origin, radius):
    ax.set_xlim3d([origin[0] - radius, origin[0] + radius])
    ax.set_ylim3d([origin[1] - radius, origin[1] + radius])
    ax.set_zlim3d([origin[2] - radius, origin[2] + radius])


def set_axes_equal(ax):
    '''Make axes of 3D plot have equal scale so that spheres appear as spheres,
    cubes as cubes, etc..  This is one possible solution to Matplotlib's
    ax.set_aspect('equal') and ax.axis('equal') not working for 3D.

    Input
      ax: a matplotlib axis, e.g., as output from plt.gca().
    '''

    limits = np.array([
        ax.get_xlim3d(),
        ax.get_ylim3d(),
        ax.get_zlim3d(),
    ])

    origin = np.mean(limits, axis=1)
    radius = 0.5 * np.max(np.abs(limits[:, 1] - limits[:, 0]))
    set_axes_radius(ax, origin, radius)


def hyp_part1(x, y, z):
    return (x ** 2) + (y ** 2) + (z ** 2) - 10000


fig = plt.figure()
ax: Axes3D = fig.add_subplot(111, projection='3d')

x_range = np.arange(-100, 100, 1)
y_range = np.arange(-100, 100, 1)
z_range = np.arange(-100, 100, 1)
X, Y, Z = np.meshgrid(x_range, y_range, z_range)
A = np.linspace(-100, 100, 20)

A1, A2 = np.meshgrid(A, A)

for z in A:
    X, Y = A1, A2
    Z = hyp_part1(X, Y, z)
    ax.contour(X, Y, Z + z, [z], zdir='z', color="r")

for y in A:
    X, Z = A1, A2
    Y = hyp_part1(X, y, Z)
    ax.contour(X, Y + y, Z, [y], zdir='y')

for x in A:
    Y, Z = A1, A2
    X = hyp_part1(x, Y, Z)
    ax.contour(X + x, Y, Z, [x], zdir='x')

# ax.set_aspect('equal','box')
ax.set_zlim3d(-100, 100)
ax.set_xlim3d(-100, 100)
ax.set_ylim3d(-100, 100)
# ax.axvline()
# ax.axhline()
# ax.set_aspect('equal')

# max_range = np.array([X.max()-X.min(), Y.max()-Y.min(), Z.max()-Z.min()]).max() / 2.0
# mid_x = (X.max()+X.min()) * 0.5
# mid_y = (Y.max()+Y.min()) * 0.5
# mid_z = (Z.max()+Z.min()) * 0.5
# ax.set_xlim(mid_x - max_range, mid_x + max_range)
# ax.set_ylim(mid_y - max_range, mid_y + max_range)
# ax.set_zlim(mid_z - max_range, mid_z + max_range)
# set_axes_equal(ax)
plt.show()
