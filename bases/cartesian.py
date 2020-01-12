from mpl_toolkits.axisartist import AxisArtist
from mpl_toolkits.axisartist.axislines import SubplotZero, Axes
import matplotlib.pyplot as plt
from numpy import *


# Coord(object)表示继承于object
class Coord:
    G: mat
    ax: Axes
    g1: array
    g2: array
    color = "black"
    Gi: mat
    Gd: mat

    def __init__(self, ax: Axes, g1: array, g2: array, color="black"):
        # print("coord=", g1, g2)
        # 协变分量的两个基向量为列构成的矩阵,要转置一下，否则方向不对
        # G = mat([g1, g2]).T
        self.G = mat([g1, g2]).T
        # 基向量矩阵的逆矩阵，用来将向量的笛卡尔读数转换成斜角读数
        self.Gi = self.G.I
        # 对偶坐标系的基向量矩阵是逆矩阵的转置。这是由对偶坐标系的定义得来的？gi*gi=1, gi*gj=0
        self.Gd = self.Gi.T
        self.g1 = g1
        self.g2 = g2
        self.ax = ax
        self.color = color

    # 绘制斜角坐标系
    def draw_basis(self):
        # 以第一列为起点，第二列为终点, 第三个参数是颜色
        # linestyle='dashed'
        # ax.plot([0, G[0, 0]],
        #         [0, G[1, 0]],
        #         color=color
        #         )
        max_scale = 10
        for i in range(max_scale):
            self.ax.scatter(self.g1[0] * i, self.g1[1] * i, color="blue")
            self.ax.scatter(self.g2[0] * i, self.g2[1] * i, color="blue")

        self.ax.plot([0, self.g1[0] * max_scale],
                     [0, self.g1[1] * max_scale],
                     color=self.color
                     )
        self.ax.plot([0, self.g2[0] * max_scale],
                     [0, self.g2[1] * max_scale],
                     color=self.color
                     )

    # 求向量在斜角坐标中的读数。
    def get_xy_for_vector(self, vector: array) -> array:
        vv = self.Gi @ vector
        v = [vv[0, 0], vv[0, 1]]
        return v

    # 绘制一个向量的在当前斜角坐标的分量
    def draw_components_for_vector(self, vector: array):
        v = self.get_xy_for_vector(vector)
        # 将斜角读数转化为笛卡尔读数
        # 这个算式的意思是将g1乘以x倍后得到的向量在笛卡尔坐标系的读数。
        c1 = self.g1 * v[0]
        c2 = self.g2 * v[1]
        # 从基向量的分量的笛卡尔坐标点，朝着向量所在点绘制虚线
        self.ax.plot([c1[0], vector[0]],
                     [c1[1], vector[1]],
                     color=self.color,
                     linestyle="dashed"
                     )
        self.ax.plot([c2[0], vector[0]],
                     [c2[1], vector[1]],
                     color=self.color,
                     linestyle="dashed"
                     )

    # 获取对偶坐标系。 因为是在定义过程中，所以Coord还没有? 声明一个Coord: pass
    def get_dual_coord(self, color="black") -> 'Coord':
        # 逆变坐标系
        # 要是直接能用1/g1得出rg1就好了。这是不行的，不仅要g1*rg1=1, 还要g1*rg2=0
        rg1 = array(get_column_from_matrix(self.Gd, 0))
        rg2 = array(get_column_from_matrix(self.Gd, 1))
        dual_coord = Coord(self.ax, rg1, rg2, color)
        return dual_coord


# 初始化坐标系
def init_cartesian_coord(min_size=-2, max_size=8) -> Axes:
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


def get_column_from_matrix(m: mat, c: int) -> array:
    return array([m[0, c], m[1, c]])
