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
UNIT = 1
MAX = 12

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
        for col in range(0, MAX):
            # 为一个y，创建一整行的点。y值不变，x值从左到右
            if not reshape:
                x_row.append(col)
                y_row.append(row)
            else:
                # 直接计算某一个点的变形情况，这样是可以的。但这样的问题在于，没有显示出
                # 单元格的增加，某些区域的单元格看起来变大了。实际中没有这种情况。因为单元格的高度和宽度
                # 只会变小，不会变大。

                x = row
                y = col
                # 如果x==0, 没法计算y/x
                x = 0.0001 if x == 0 else x
                a = y/x
                # 计算当前到圆心的距离
                r = (y**2 + x**2)**0.5
                # 缩短这个距离
                r1 = r - r * (np.e ** (-r/2))
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
