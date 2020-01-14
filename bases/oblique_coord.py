from mpl_toolkits.axisartist.axislines import Axes
from numpy import *

from bases.cartesian import Cartesian
from bases.common import get_column_from_matrix


class ObliqueCoord:
    g1: array
    g2: array
    # 这三个矩阵是什么关系呢？
    # 本坐标系的两个基向量在笛卡尔坐标系中的读数矩阵(列分别是g1,g2)，
    G: mat
    # 变形矩阵的逆矩阵，用来将笛卡尔坐标读数转换成本坐标系的读数
    # 逆矩阵的几何意义又是什么？也值得追问。只有逆矩阵，没有逆向量。

    # 逆矩阵是对基向量的反向操作，如果g1在x方向放大a倍，逆矩阵则缩小a倍，
    # 如果基向量移动了x轴，则逆矩阵要讲x轴移动回去。
    # 求逆矩阵，可以尝试用Ma=b, 然后找到一个矩阵使得a = M1b, M1就是M的逆矩阵。
    # 这个式子的含义是，找到一个对向量b进行变形的矩阵，让变形后的结果刚好与a相同。这个矩阵就是M的逆矩阵
    # 感觉逆矩阵就是矩阵的除法。一个算式除以某个矩阵，等价于它乘以这个矩阵的逆矩阵。
    # 这样说，逆矩阵的几何意义，也可说是消除坐标变形。
    
    # 但逆矩阵的运算颇为复杂，因为你对一个基向量的一个分量的变动，还会影响另一个基向量的分量，所以不是直接修改基向量的分量那么简单。
    G_inverse: mat
    # 对偶坐标系的两个基向量笛卡尔读数构成的矩阵
    G_dual: mat
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
        self.G_inverse = self.G.I
        # 对偶坐标系的基向量矩阵是逆矩阵的转置。
        # 这是由对偶坐标系的定义得来的: gi*gi=1, gi*gj=0，逆矩阵的转置符合这个性质（这又是为什么？）
        self.G_dual = self.G_inverse.T
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

    def to_cartesian_components(self, vector_in_oblique: array) -> array:
        """
        给一个向量的斜角读数，获取这个向量的笛卡尔读数
        
        为什么一个向量的斜角读数左乘基向量矩阵，可以得到笛卡尔坐标读数呢？
        用向量加法来解释。
        已知一个向量的斜角读数，表示这个向量沿两个基向量分解成两个向量，分别是基向量g1的x倍， g2的y倍。
        其笛卡尔坐标系读数分别是x*g1，y*g2，那么这个向量本身的笛卡尔读数就是x*g1+y*g2

        向量加法比较简单直观，直接绘制x1+x2, y1+y2就可以看出来了。也可以说，这正是向量加法的定义。
        :param vector_in_oblique:
        :return:
        """
        # vv = self.G @ vector_in_oblique
        # print(vv)
        # return array([vv[0, 0], vv[0, 1]])

        # 这样更好理解
        x = vector_in_oblique[0]
        y = vector_in_oblique[1]
        vc = self.g1 * x + self.g2 * y
        return vc

    def to_oblique_components(self, vector_in_cartesian: array) -> array:
        """
        获取笛卡尔向量在斜角坐标中的读数。
        基向量的"逆向量"，构成了矩阵G_inverse

        这个运算很让人费解。不像从斜角到笛卡尔读数那么直观。
        逆矩阵的列如果是基向量，它的含义是什么呢？ 《线性代数的本质》里面，并不是通过对斜角坐标做
        逆运算，而是对笛卡尔坐标做变形，记录变形过程，当变形结果与斜角坐标刚好互逆的时候，就得到了逆矩阵

        :param vector_in_cartesian: 笛卡尔向量
        :return: 斜角坐标读数
        """
        vv = self.G_inverse @ vector_in_cartesian
        v = array([vv[0, 0], vv[0, 1]])
        return v

    def draw_oblique_components(self, vector_in_cartesian: array):
        """
        绘制一个向量的在当前斜角坐标的分量
        :param vector_in_cartesian: 笛卡尔向量
        """
        v = self.to_oblique_components(vector_in_cartesian)
        # 将斜角读数转化为笛卡尔读数
        # 这个算式的意思是将g1乘以x倍后得到的向量在笛卡尔坐标系的读数。
        c1 = self.g1 * v[0]
        c2 = self.g2 * v[1]
        # 从基向量的分量的笛卡尔坐标点，朝着向量所在点绘制虚线
        self.ax.plot([c1[0], vector_in_cartesian[0]],
                     [c1[1], vector_in_cartesian[1]],
                     color=self.color,
                     linestyle="dashed"
                     )
        self.ax.plot([c2[0], vector_in_cartesian[0]],
                     [c2[1], vector_in_cartesian[1]],
                     color=self.color,
                     linestyle="dashed"
                     )

    def get_dual_coord(self, color="black") -> 'ObliqueCoord':
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
        rg1 = array(get_column_from_matrix(self.G_dual, 0))
        rg2 = array(get_column_from_matrix(self.G_dual, 1))
        dual_coord = ObliqueCoord(self.cartesian, rg1, rg2, color)
        return dual_coord


