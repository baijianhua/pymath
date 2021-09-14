import numpy as np
import matplotlib.pyplot as plt
from matplotlib.collections import LineCollection
from sympy import symbols, cos, sin
from sympy.diffgeom import Manifold, Patch, CoordSystem

EDGE = 2
STEP = 8 * EDGE + 1

rect: CoordSystem
polar: CoordSystem


def plot_grid(x, y, ax=None, **kwargs):
    ax = ax or plt.gca()
    segs1 = np.stack((x, y), axis=2)
    segs2 = segs1.transpose(1, 0, 2)
    ax.add_collection(LineCollection(segs1, **kwargs))
    ax.add_collection(LineCollection(segs2, **kwargs))
    ax.autoscale()


def f2(xx: np.array, yy: np.array):
    # global rect
    # global polar

    uu = []
    vv = []
    for i in range(0, len(xx)):
        ui = []
        vi = []
        for j in range(0, len(xx[i])):
            x = xx[i][j]
            y = yy[i][j]
            u = x ** 2
            v = y ** 2
            ui.append(u)
            vi.append(v)

        uu.append(ui)
        vv.append(vi)
    return uu, vv


def main():
    fig, ax = plt.subplots()
    ax.set_aspect('equal')
    grid_x, grid_y = np.meshgrid(np.linspace(0, EDGE, STEP), np.linspace(0, EDGE, STEP))
    plot_grid(grid_x, grid_y, ax=ax, color="lightgrey")

    distx, disty = f2(grid_x, grid_y)
    plot_grid(distx, disty, ax=ax, color="C0")

    plt.show()


main()
