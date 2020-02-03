# https://stackoverflow.com/questions/47295473/how-to-plot-using-matplotlib-python-colahs-deformed-grid

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.collections import LineCollection


def plot_grid(x, y, ax=None, **kwargs):
    ax = ax or plt.gca()
    segs1 = np.stack((x, y), axis=2)
    segs2 = segs1.transpose(1, 0, 2)
    ax.add_collection(LineCollection(segs1, **kwargs))
    ax.add_collection(LineCollection(segs2, **kwargs))
    ax.autoscale()


def f(x, y):
    u = x
    v = y
    return u - np.exp(-u ** 2 - v ** 2), v - np.exp(-u ** 2 - v ** 2)


fig, ax = plt.subplots()

ax.set_aspect('equal')
grid_x, grid_y = np.meshgrid(np.linspace(-3, 3, 20), np.linspace(-3, 3, 20))
plot_grid(grid_x, grid_y, ax=ax, color="lightgrey")

distx, disty = f(grid_x, grid_y)
plot_grid(distx, disty, ax=ax, color="C0")

plt.show()
