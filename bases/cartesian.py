from mpl_toolkits.axisartist import AxisArtist
from mpl_toolkits.axisartist.axislines import SubplotZero, Axes
import matplotlib.pyplot as plt
import numpy as np


# 初始化坐标系
def init_coord(min_size=-2, max_size=8) -> Axes:
    # max_size = 8
    # min_size = -2
    # 本身就应该已经有一个plot了。这个plt可以通过调用figure，来构造一个新的图形。
    # fig可以通过add_subplot，为自己添加一个坐标系
    # 绘图是以坐标系为基础的。
    fig = plt.figure(figsize=(max_size - min_size, max_size - min_size))
    ax: Axes = SubplotZero(fig, 111)
    fig.add_subplot(ax)

    ticks = [i for i in range(min_size, max_size) if i != 0]
    # xaxis又不是AxisArtist，那它是什么类型？ Axes又和Axis不同，这是两个什么东西呢？
    ax.xaxis.set_ticks(ticks)
    ax.yaxis.set_ticks(ticks)
    ax.grid(True)
    ax.set_xlim(min_size, max_size)
    ax.set_ylim(min_size, max_size)

    for direction in ["xzero", "yzero"]:
        # adds arrows at the ends of each axis
        axis: AxisArtist = ax.axis[direction]
        axis.set_axisline_style("->")
        axis.set_visible(True)

    for direction in ["left", "right", "bottom", "top"]:
        # hides borders
        ax.axis[direction].set_visible(False)

    return ax


def draw_basis(ax: Axes, G: np.matrix, color="black"):
    ax.plot([0, G[0, 0]],
            [0, G[1, 0]],
            color=color
            )
    ax.plot([0, G[0, 1]],
            [0, G[1, 1]],
            color=color
            )


