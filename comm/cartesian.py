from matplotlib import pyplot as plt
from mpl_toolkits.axisartist import Axes, SubplotZero, AxisArtist
from numpy import *

class Cartesian:
    ax: Axes

    def __init__(self, min_size=-2, max_size=8):
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
        fig = plt.figure(figsize=(max_size - min_size, max_size - min_size), dpi=72)
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

    def draw_vector(self, point: array, with_components=False, color="black"):
        """
        在笛卡尔坐标系中绘制向量
        :param color:
        :param point:
        :param with_components: 是否绘制笛卡尔分量
        :return:
        """
        self.ax.plot([0, point[0]],
                     [0, point[1]], color=color, linewidth=2)
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
