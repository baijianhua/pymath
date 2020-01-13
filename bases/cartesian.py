from mpl_toolkits.axisartist import AxisArtist
from mpl_toolkits.axisartist.axislines import SubplotZero, Axes
import matplotlib.pyplot as plt
from numpy import *


# Coord(object)表示继承于object
class Coord:
    g1: array
    g2: array
    # 本坐标系的两个基向量在笛卡尔坐标系中的读数矩阵，用来将本坐标系的读数转换成笛卡尔读数
    G: mat
    # 用来将笛卡尔坐标读数转换成本坐标系的读数
    Gi: mat
    # 对偶坐标系的两个基向量笛卡尔读数构成的矩阵
    Gd: mat
    # matplotlib 画布
    ax: Axes
    color = "black"
    cartesian: 'Cartesian'

    def __init__(self, coord: 'Cartesian', g1: array, g2: array, color="black"):
        """
        用两个基向量构成一个新的坐标系
        :param coord: 笛卡尔坐标系。包含了坐标边界以及Axes对象
        :param g1: 基向量
        :param g2: 基向量
        :param color: 坐标轴和分量的颜色
        """

        # 协变分量的两个基向量为列构成的矩阵,要转置一下，否则方向不对
        self.G = mat([g1, g2]).T
        # 基向量矩阵的逆矩阵，用来将向量的笛卡尔读数转换成斜角读数
        self.Gi = self.G.I
        # 对偶坐标系的基向量矩阵是逆矩阵的转置。这是由对偶坐标系的定义得来的？gi*gi=1, gi*gj=0
        self.Gd = self.Gi.T
        self.g1 = g1
        self.g2 = g2
        self.ax = coord.ax
        self.color = color
        self.cartesian = coord

    def draw_basis(self):
        """
        绘制斜角坐标系
        以第一列为起点，第二列为终点, 第三个参数是颜色
        linestyle='dashed'
        ax.plot([0, G[0, 0]],
                [0, G[1, 0]],
                color=color
                )

        :return:
        """
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

    def get_cartesian_compoents(self, vector: array) -> array:
        """
        获取斜角向量的笛卡尔读数
        :param vector:
        :return:
        """
        vv = self.G @ vector
        return array([vv[0, 0], vv[0, 1]])

    def get_components(self, vector: array) -> array:
        """
        获取笛卡尔向量在斜角坐标中的读数。
        :param vector: 笛卡尔向量
        :return: 斜角坐标读数
        """
        vv = self.Gi @ vector
        v = array([vv[0, 0], vv[0, 1]])
        return v

    def draw_components(self, vector: array):
        """
        绘制一个向量的在当前斜角坐标的分量
        :param vector: 笛卡尔向量
        """

        v = self.get_components(vector)
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

    def get_dual_coord(self, color="black") -> 'Coord':
        """
        获取对偶坐标系

        什么叫协变坐标系？什么叫逆变坐标系？这应该是没有标准定义的，
        锐角、基向量模长小于1，这些定义都不行。
        如果坐标系的基向量一个小于1，一个大于1会怎样？这就没法说整个坐标系是逆变，还是协变了
        对偶坐标系（逆变？）

        要是直接能用1/g1得出rg1就好了。这是不行的，不仅要g1*rg1=1, 还要g1*rg2=0
        :param color:
        :return: 'Coord' 对偶坐标系
        """
        rg1 = array(get_column_from_matrix(self.Gd, 0))
        rg2 = array(get_column_from_matrix(self.Gd, 1))
        dual_coord = Coord(self.cartesian, rg1, rg2, color)
        return dual_coord


class Cartesian:
    ax: Axes

    def __init__(self,min_size=-2, max_size=8):
        """
        初始化整个屏幕的范围。绘制笛卡尔坐标轴、刻度、网格
        :param min_size: 负值，x y坐标轴的最小值
        :param max_size: 正值，x y的最大值
        """
        # max_size = 8
        # min_size = -2
        # 本身就应该已经有一个plot了。这个plt可以通过调用figure，来构造一个新的图形。
        # fig可以通过add_subplot，为自己添加一个坐标系
        # 绘图是以坐标系为基础的。
        fig = plt.figure(figsize=(max_size - min_size, max_size - min_size))
        self.ax = SubplotZero(fig, 111)
        fig.add_subplot(self.ax)

        # xaxis又不是AxisArtist，那它是什么类型？ Axes又和Axis不同，这是两个什么东西呢？
        # 显示刻度
        ticks = [i for i in range(min_size, max_size) if i != 0]
        self.ax.xaxis.set_ticks(ticks)
        self.ax.yaxis.set_ticks(ticks)
        # 锁定纵横比
        self.ax.set_aspect("equal")
        # 显示网格
        self.ax.grid(True)
        self.ax.set_xlim(min_size, max_size)
        self.ax.set_ylim(min_size, max_size)

        for direction in ["xzero", "yzero"]:
            # adds arrows at the ends of each axis
            axis: AxisArtist = self.ax.axis[direction]
            axis.set_axisline_style("->")
            axis.set_visible(True)

        for direction in ["left", "right", "bottom", "top"]:
            # hides borders
            self.ax.axis[direction].set_visible(False)

    def draw_vector(self, point: [], with_components=False):
        """
        在笛卡尔坐标系中绘制向量
        :param point:
        :param with_components: 是否绘制笛卡尔分量
        :return:
        """
        self.ax.plot([0, point[0]],
                     [0, point[1]], color="black", linewidth=2)
        if with_components:
            self.draw_components(point)

    def draw_components(self, point: []):
        """
        绘制一个向量的笛卡尔坐标分量
        从表示向量的点，分别向两个坐标轴绘制虚线
        """
        self.ax.plot([point[0], point[0]],
                     [point[1], 0], color="black", linestyle="dashed")
        self.ax.plot([point[0], 0],
                     [point[1], point[1]], color="black", linestyle="dashed")


def get_column_from_matrix(m: mat, c: int) -> array:
    """
    取矩阵的某一列
    :param m:
    :param c:
    :return:
    """
    return array([m[0, c], m[1, c]])
