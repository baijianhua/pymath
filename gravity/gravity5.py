# https://stackoverflow.com/questions/47295473/how-to-plot-using-matplotlib-python-colahs-deformed-grid

"""
仍然有缺陷
1. 靠近边缘变化太剧烈
2. 靠近边缘的侵占而不是挤压后面的图形
3. 1 1 这个格点绘制的很奇怪
4. 靠近两个坐标轴的，坐标轴方向压缩了，另一个坐标轴方向却放大了。这感觉好像不太对呀。应该是各个方向都压缩
但如果是各个方向都压缩，那要如何绘制呢？如果一个区域，各个单元格都缩小了，那就会产生空隙，这感觉也不对。
或者是不是必须沿着半径方向被压缩，垂直于半径的方向被拉伸呢？
其实拉伸也是相对于原来位置，拉伸后的幅度，仍然小于本位置的幅度？
"""
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.collections import LineCollection
from sympy import symbols, cos, sin
from sympy.diffgeom import Manifold, Patch, CoordSystem

EDGE = 2
STEP = 8*EDGE+1
# SCALE = 0.1
R = 1

rect: CoordSystem
polar: CoordSystem


def plot_grid(x, y, ax=None, **kwargs):
    ax = ax or plt.gca()
    segs1 = np.stack((x, y), axis=2)
    segs2 = segs1.transpose(1, 0, 2)
    ax.add_collection(LineCollection(segs1, **kwargs))
    ax.add_collection(LineCollection(segs2, **kwargs))
    ax.autoscale()


def define_coord_sys():
    global rect
    global polar
    """定义Manifold, Patch, CoordSystem"""
    r, theta = symbols('r, theta')
    x, y = symbols('x, y')
    m = Manifold('M', 2)
    # 定义一个patch
    patch = Patch('P', m)
    # 为这个patch建立坐标系，一个是笛卡尔，一个是极坐标
    rect = CoordSystem('rect', patch)
    polar = CoordSystem('polar', patch)
    polar.connect_to(rect, [r, theta], [r * cos(theta), r * sin(theta)])
    # return rect, polar


def sig(i):
    # return 1
    return -1 if (i < 0) else 1


def dist(x, y):
    # print(x, y, R)
    d = (x ** 2 + y ** 2 - R ** 2)
    # print(x, y, R, d)
    return d if d > 0 else 0


def f2(xx: np.array, yy: np.array):
    # global rect
    # global polar

    uu = []
    vv = []
    for i in range(0, len(xx)):
        ui = []
        vi = []
        for j in range(0, len(xx[i])):
            # 这样取到的是网格中每个点的坐标，逐行取，从左到右。
            r = R
            theta = 0
            r1 = R
            x = xx[i][j]
            y = yy[i][j]
            exp = 0
            modifier = 1
            if x == 0 and y == 0:
                u = R
                v = R
            else:
                # r, theta
                if y == 0:
                    r = x
                    theta = 0
                else:
                    r, theta = rect.coord_tuple_transform_to(polar, [x, y])

                exp = r
                # 修正系数最大是1，递减趋向于0, 这样的函数是指数函数，当自变量为0，结果是1，自变量从0开始减小，结果趋向于0
                modifier = (np.e ** -exp)
                # modifier衰减太厉害，导致第一个点的坐标值比第二个点还靠外面。永远靠近外面，但不应该比外面的大。
                # +R又不对，因为R的值要衰减，最大是R, 到远处就变美了
                # 这个增加的值从R开始，不断让R乘以一个小于1大于0的数。累加起来。但只能沿着一个方向累加。
                r1 = r + R * modifier
                u, v = polar.coord_tuple_transform_to(rect, [r1, theta])

            print("x=", x, "y=", y, "u=", u, "v=", v,
                  "r=", r,  "r1=", r1, "theta=", theta,
                  "exp=", exp, "modifier=", modifier)

            # u = x
            # 除以np.e ** x， 让y的偏移量随着x的增大而变小
            # v = y
            # / (np.e ** (xx))
            # v = y
            ui.append(u)
            vi.append(v)
            # vi.append(yy)
            # ui.append(xx)

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


define_coord_sys()
main()
