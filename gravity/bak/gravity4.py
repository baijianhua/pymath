# https://stackoverflow.com/questions/47295473/how-to-plot-using-matplotlib-python-colahs-deformed-grid

"""
这个形状仍然不对。靠近坐标轴的地方变化太大。不管是横轴还是纵轴。应该是以原点为圆心，各个网格均匀分担才对
而不管是否靠近坐标轴
"""
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.collections import LineCollection

EDGE = 2
STEP = 2 * EDGE + 1
SCALE = 0.1

R = 2


def plot_grid(x, y, ax=None, **kwargs):
    ax = ax or plt.gca()
    segs1 = np.stack((x, y), axis=2)
    segs2 = segs1.transpose(1, 0, 2)
    ax.add_collection(LineCollection(segs1, **kwargs))
    ax.add_collection(LineCollection(segs2, **kwargs))
    ax.autoscale()


def sig(i):
    # return 1
    return -1 if (i < 0) else 1


def dist(x, y):
    d = (x ** 2 + y ** 2) - R ** 2
    return d if d >= 0 else 0


def f2(x: np.array, y: np.array):
    u = []
    v = []
    for i in range(0, len(x)):
        ui = []
        vi = []
        for j in range(0, len(x[i])):
            # 这样取到的是网格中每个点的坐标，逐行取，从左到右。
            xx = x[i][j]
            yy = y[i][j]
            uu = xx
            # 坐标被r所挤压，距离r越近，挤压幅度越大，坐标可以占用别人的位置。最大移动范围是R，最小移动范围是0
            uu = xx + R * (np.e ** - dist(xx, yy)) / np.e
            # 除以np.e ** x， 让y的偏移量随着x的增大而变小
            vv = yy + R * (np.e ** - dist(xx, yy)) / np.e
            # / (np.e ** (xx))
            print(xx, yy, uu, vv, (np.e**dist(xx, yy)))
            ui.append(uu)
            vi.append(vv)
            # vi.append(yy)
            # ui.append(xx)

        u.append(ui)
        v.append(vi)
    return u, v


fig, ax = plt.subplots()
ax.set_aspect('equal')
grid_x, grid_y = np.meshgrid(np.linspace(0, EDGE, STEP), np.linspace(0, EDGE, STEP))
plot_grid(grid_x, grid_y, ax=ax, color="lightgrey")

distx, disty = f2(grid_x, grid_y)
plot_grid(distx, disty, ax=ax, color="C0")

plt.show()
