# https://stackoverflow.com/questions/47295473/how-to-plot-using-matplotlib-python-colahs-deformed-grid

"""
这个形状仍然不对。靠近坐标轴的地方变化太大。不管是横轴还是纵轴。应该是以原点为圆心，各个网格均匀分担才对
而不管是否靠近坐标轴

变形的目标，是在某处给定一个球体或者立方体，整个坐标中的网格，靠近这个物体的，受到变形影响，距离越远，影响
越小，直到可以忽略不计

但有个要求是靠近物体的网格，是均匀的受到影响，不能有的多，有的少

或许用极坐标是更好的选择？但是也不行。极坐标如何体现原有的坐标系呢？
极坐标没有平直的地方，到处都不均匀。

"""
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.collections import LineCollection

EDGE = 5
STEP = 2 * EDGE + 1


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


def f1(x: np.array, y: np.array):
    u = []
    v = []
    for i in range(0, len(x)):
        ui = []
        vi = []
        for j in range(0, len(x[i])):
            # 这样取到的是网格中每个点的坐标，逐行取，从左到右。
            xx = x[i][j]
            yy = y[i][j]
            print("x=", xx, "y=", yy)
            expn = - 0.2 * (xx ** 2 + yy ** 2)
            # 坐标越远离中心，delta越小。当x=+-1或者y=+-1,
            delta = np.exp(expn)
            print(expn)
            uu = xx if xx == 0 else xx + sig(xx) * delta
            vv = yy if yy == 0 else yy + sig(yy) * delta
            print("uu=", uu, "vv=", vv)
            ui.append(uu)
            vi.append(vv)
            # vi.append(yy)
            # ui.append(xx)

        u.append(ui)
        v.append(vi)
    return u, v


fig, ax = plt.subplots()
ax.set_aspect('equal')
grid_x, grid_y = np.meshgrid(np.linspace(-EDGE, EDGE, STEP), np.linspace(-EDGE, EDGE, STEP))
plot_grid(grid_x, grid_y, ax=ax, color="lightgrey")

distx, disty = f1(grid_x, grid_y)
plot_grid(distx, disty, ax=ax, color="C0")

plt.show()
