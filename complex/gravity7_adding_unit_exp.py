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

MAX = 10
MAX_R = (2 * (MAX ** 2))**0.5
SCALE = 1.1

rect: CoordSystem
polar: CoordSystem


def plot_grid(x, y, ax=None, **kwargs):
    ax = ax or plt.gca()
    segs1 = np.stack((x, y), axis=2)
    segs2 = segs1.transpose(1, 0, 2)
    ax.add_collection(LineCollection(segs1, **kwargs))
    ax.add_collection(LineCollection(segs2, **kwargs))
    ax.autoscale()


def create_points(reshape=False):
    # 其实先创建一堆点就可以。
    x_rows = []
    y_rows = []
    for row in range(0, MAX):
        x_row = []
        y_row = []
        for col in range(0, MAX):
            # 为一个y，创建一整行的点。y值不变，x值从左到右
            if not reshape:
                x_row.append(col)
                y_row.append(row)
            else:
                pre_x = 0 if col == 0 else x_row[col-1]
                pre_y = 0 if row == 0 else y_rows[row - 1][col]
                r = (pre_x ** 2 + pre_y ** 2)**0.5
                # 离圆心越近，缩小越严重。离得越远，unit 越接近于1
                # 现在的问题在于，靠近圆心的部分增长太慢，因为unit是从圆心算起的。
                # 如果指数值能在更小的范围内分布，就会好一些。

                # 这个算式可以保证exp在-1 到0之间, 而且不会变化很剧烈。因为 = 0才 = 1.
                # 也许时空的最大变化量也就是这么多了，一个单元的从0到1的变化。
                # 可能时空单元只有一个度量，就是光在固定周期内走过多远。只是它可以走向不同方向。
                # 假设一种基本粒子，原子、电子什么都可以，它有度量，同时又有周期，光在一个固定周期
                # 能够穿过的粒子的数量，就是我们的时空。

                # 从0到1这个度量变化，足够容纳任意大的空间，因为可以从无穷小开始。

                exp = (r - MAX_R) / MAX_R
                x_unit = 3 ** exp + 0.37
                print("exp=", exp, "r=", r, "MAX_R", MAX_R, "SCALE=", SCALE, "x_unit=", x_unit)
                y_unit = x_unit
                x = 0 if col == 0 else pre_x + x_unit
                y = 0 if row == 0 else pre_y + y_unit
                # print("row=", row, "col=", col, "pre_x", pre_x, "pre_y=", pre_y,
                #       "x=", x, "y=", y)

                x_row.append(x)
                y_row.append(y)

        print("row end-------------------------")
        x_rows.append(x_row)
        y_rows.append(y_row)

    return x_rows, y_rows


def main():
    fig, ax = plt.subplots()
    ax.set_aspect('equal')
    x_rows, y_rows = create_points()
    plot_grid(x_rows, y_rows, ax=ax, color="lightgrey")

    x_rows, y_rows = create_points(True)
    plot_grid(x_rows, y_rows, ax=ax, color="blue")
    plt.show()


main()
