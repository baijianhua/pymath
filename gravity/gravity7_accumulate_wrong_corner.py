"""
这个图形还是有问题的。对角线位置绘制的不对。所有方位的度量，都要小于原有度量。
而这个图里面，有的地方对角线的长度大于原来的度量。

而且这个图里面，没有办法渐渐的恢复平直
"""
from typing import List
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.collections import LineCollection
from sympy.diffgeom import Manifold, Patch, CoordSystem

EDGE = 2
STEP = 8*EDGE+1
R = 1
UNIT = 1
MAX = 20

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
    last_y = -1
    for row in range(0, MAX):
        x_row = []
        y_row = []
        last_x = -1
        accumulate_x = 0
        col_range: List = [*range(0, MAX)]  # *表示将表达式展开
        # col_range = range(0, MAX)
        for col in col_range:
            # 为一个y，创建一整行的点。y值不变，x值从左到右
            if not reshape:
                x_row.append(col)
                y_row.append(row)
            else:
                # 从上一列取出历史x, 以显示x的累计变形效果
                # 从上一行里面取出历史的y, 这样才能显示累计的变形效果
                # 这个图形应该是接近正确的，但问题是怎么样才能让他恢复平直呢？ 要在什么地方加入新的单元格？
                # 这个思考起来应该是比较简单的。可以考虑在累计缺1的情况下加入一个单元格，但有个问题是斜的方向怎么办？
                x = last_x + 1
                y = 0 if row == 0 else y_rows[row-1][col]+1
                print("x=", row)
                # 如果x==0, 没法计算y/x
                x = 0.0001 if x == 0 else x
                a = y/x
                # 计算当前到圆心的距离
                r = (y**2 + x**2)**0.5
                # 缩短这个距离
                r1 = r - r * (np.e ** (-r/1.2))
                # 计算调整过后的x, y坐标
                x1 = (r1**2/(1+a**2))**0.5
                y1 = a*x1
                last_x = x1
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
    plot_grid(x_rows, y_rows, ax=ax, color="lightgrey")

    x_rows, y_rows = create_points(True)
    plot_grid(x_rows, y_rows, ax=ax, color="blue")
    plt.show()


main()
