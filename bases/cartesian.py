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

    # xaxis又不是AxisArtist，那它是什么类型？ Axes又和Axis不同，这是两个什么东西呢？
    # 显示刻度
    ticks = [i for i in range(min_size, max_size) if i != 0]
    ax.xaxis.set_ticks(ticks)
    ax.yaxis.set_ticks(ticks)
    # 锁定纵横比
    ax.set_aspect("equal")
    # 显示网格
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
    # 以第一列为起点，第二列为终点, 第三个参数是颜色
    # linestyle='dashed'
    # ax.plot([0, G[0, 0]],
    #         [0, G[1, 0]],
    #         color=color
    #         )
    max_scale = 10
    g1 = get_column_from_matrix(G, 0)
    g2 = get_column_from_matrix(G, 1)

    for i in range(max_scale):
        ax.scatter(g1[0] * i, g1[1] * i, color="blue")
        ax.scatter(g2[0] * i, g2[1] * i, color="blue")

    ax.plot([0, g1[0] * max_scale],
            [0, g1[1] * max_scale],
            color=color
            )
    ax.plot([0, g2[0] * max_scale],
            [0, g2[1] * max_scale],
            color=color
            )
    # ax.scatter(4, 3, color="blue")
    # 怎么绘制坐标的刻度呢？


def draw_vector(ax: Axes, point: [], with_components=False):
    ax.plot([0, point[0]],
            [0, point[1]], color="black", linewidth=2)
    if with_components:
        draw_components(ax, point)


def draw_components(ax: Axes, point: []):
    # 从表示向量的点，分别向两个坐标轴绘制虚线
    ax.plot([point[0], point[0]],
            [point[1], 0], color="black", linestyle="dashed")
    ax.plot([point[0], 0],
            [point[1], point[1]], color="black", linestyle="dashed")


def get_column_from_matrix(m: np.mat, c: int) -> np.array:
    return np.array([m[0, c], m[1, c]])


def draw_components_in_coord(ax: Axes, v: np.array, G: np.mat, color="black"):
    g1 = get_column_from_matrix(G, 0)
    g2 = get_column_from_matrix(G, 1)
    # x*g1, 即x个g1, 可以得到斜角坐标系的x分量，在笛卡尔坐标系的读数，即g1v.
    g1v = g1 * v[0]
    g2v = g2 * v[1]
    # 从基向量的分量的笛卡尔坐标点，朝着向量所在点绘制虚线
    ax.plot([g1v[0], v[0]],
            [g1v[1], v[1]],
            color=color,
            linestyle="dashed"
            )
    ax.plot([g2v[0], v[0]],
            [g2v[1], v[1]],
            color=color,
            linestyle="dashed"
            )
