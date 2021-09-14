# https://stackoverflow.com/questions/47295473/how-to-plot-using-matplotlib-python-colahs-deformed-grid

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.collections import LineCollection

EDGE = 3
STEP = 20


def plot_grid(x, y, ax=None, **kwargs):
    ax = ax or plt.gca()
    segs1 = np.stack((x, y), axis=2)
    segs2 = segs1.transpose(1, 0, 2)
    ax.add_collection(LineCollection(segs1, **kwargs))
    ax.add_collection(LineCollection(segs2, **kwargs))
    ax.autoscale()


def sig(i):
    return -1 if (i < 0) else 1


def f(x, y):
    u = x
    v = y
    return u - np.exp(-u ** 2 - v ** 2), v - np.exp(-u ** 2 - v ** 2)


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
            expn = - (xx ** 2 + yy ** 2)
            # 坐标越远离中心，delta越小。当x=+-1或者y=+-1,
            delta = np.exp(expn)
            print(expn)
            ui.append(xx + sig(xx) * delta)
            vi.append(yy + sig(yy) * delta)

        u.append(ui)
        v.append(vi)
    return u, v


# def f1(x: np.array, y: np.array):
#     u = []
#     v = []
#     for i in range(0, len(x)):
#         ui = []
#         vi = []
#         for j in range(0, len(x[i])):
#             print(x[i][j])
#             ui.append(x[i][j] + sig(x[i][j]) * np.exp(-(x[i][j]**2 + y[i][j]**2)))
#             vi.append(y[i][j] + sig(y[i][j]) * np.exp(-x[i][j]**2 - y[i][j]**2))
#
#         u.append(ui)
#         v.append(vi)
#     return u, v


fig, ax = plt.subplots()
ax.set_aspect('equal')
# 需要弄清楚这里产生的是什么结果？不是一个二维数组！
# 第一个数据是x坐标的集合。每一个元素是
#
grid_x, grid_y = np.meshgrid(np.linspace(-EDGE, EDGE, STEP), np.linspace(-EDGE, EDGE, STEP))
# print(grid_x)
print("-----------------")
# print(grid_y)
plot_grid(grid_x, grid_y, ax=ax, color="lightgrey")

distx, disty = f(grid_x, grid_y)
plot_grid(distx, disty, ax=ax, color="C0")

# distx, disty = f1(grid_x, grid_y)
# plot_grid(distx, disty, ax=ax, color="C0")


plt.show()
