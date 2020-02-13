# https://stackoverflow.com/questions/47295473/how-to-plot-using-matplotlib-python-colahs-deformed-grid

"""
反向绘制。远处是基本上平直的。靠近物体的部分，会缩短，从后面开始累加这些缩短
的量，物质所在区域会产生一个空缺。
"""
from typing import List

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.collections import LineCollection
from sympy import symbols, cos, sin
from sympy.diffgeom import Manifold, Patch, CoordSystem

MAX = 4

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
    points = []
    x_rows = []
    y_rows = []
    last_y = -1
    for row in reversed(range(0, MAX + 1)):
        x_row = []
        y_row = []
        col_range: List = [*range(0, MAX + 1)]  # *表示将表达式展开
        # col_range = range(0, MAX)
        for col in reversed(col_range):
            # 为一个y，创建一整行的点。y值不变，x值从左到右
            if not reshape:
                x_row.append(col)
                y_row.append(row)
            else:
                # 从上一列取出历史x, 以显示x的累计变形效果
                # 从上一行里面取出历史的y, 这样才能显示累计的变形效果
                # 这个图形应该是接近正确的，但问题是怎么样才能让他恢复平直呢？ 要在什么地方加入新的单元格？
                # 这个思考起来应该是比较简单的。可以考虑在累计缺1的情况下加入一个单元格，但有个问题是斜的方向怎么办？

                # print("x_row_count=", len(x_rows))
                x = MAX if col == MAX else x_row[MAX - col - 1]
                y = MAX if row == MAX else y_rows[MAX - row - 1][MAX - col - 1]
                if x == MAX and y == MAX:
                    x_row.append(x)
                    y_row.append(y)
                else:
                    print("row=", row, "col=", col, "x=", x, "y=", y)
                    x = 0.0001 if x == 0 else x
                    # a = y / x
                    # 计算当前到圆心的距离
                    r = (y ** 2 + x ** 2) ** 0.5 - 1
                    # 缩短这个距离
                    r_shrink = r - r * (np.e ** (-r / 1.2))
                    # delta_r = r - r_shrink
                    # 计算调整过后的x, y坐标
                    x1 = r_shrink/r * x
                    y1 = r_shrink/r * y
                    # (r_shrink ** 2 / (1 + a ** 2)) ** 0.5
                    # y1 = a * x1
                    # last_x = x1
                    print("x1=", x1, "y1=", y1, "r=", r,  "r1=", r_shrink)
                    x_row.append(x1)
                    y_row.append(y1)

        print("row end-------------------------")
        x_rows.append(x_row)
        y_rows.append(y_row)

    return x_rows, y_rows


def main():
    fig, ax = plt.subplots()
    ax.set_aspect('equal')
    x_rows, y_rows = create_points()
    print(x_rows, y_rows)
    plot_grid(x_rows, y_rows, ax=ax, color="lightgrey")
    x_rows, y_rows = create_points(True)
    plot_grid(x_rows, y_rows, ax=ax, color="blue")

    plt.show()


main()
