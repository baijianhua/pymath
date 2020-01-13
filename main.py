# https://matplotlib.org/3.1.1/tutorials/toolkits/axisartist.html
import matplotlib.pyplot as plt
from bases.cartesian import Coord, Cartesian
from numpy import *

cartesian = Cartesian(-2, 6)
# 用numpy的array而非python原生array,来方便做向量与标量的乘法，否则很麻烦
# 协变坐标系
g1 = array([0.6, 0.2])
g2 = array([0.2, 1.7])
co_coord = Coord(cartesian, g1, g2, "red")

contra_coord = co_coord.get_dual_coord(color="blue")
co_coord.draw_basis()
contra_coord.draw_basis()

# 接下来如何显示向量以及它在不同坐标系下面的分量？
vector = array([2, 2])
v1 = co_coord.get_components(vector)
v2 = contra_coord.get_components(vector)
print("笛卡尔读数", vector)
print("斜角读数", v1)
print("对偶读数", v2)
print("斜角和对偶点乘", v1@v2)

cartesian.draw_vector(vector, with_components=True)
co_coord.draw_components(vector)
contra_coord.draw_components(vector)

plt.show()

