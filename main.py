# https://matplotlib.org/3.1.1/tutorials/toolkits/axisartist.html
import matplotlib.pyplot as plt
from bases.cartesian import init_cartesian_coord, draw_vector, get_column_from_matrix, Coord
from numpy import *


ax = init_cartesian_coord(-2, 6)
# 用numpy的array而非python原生array,来方便做向量与标量的乘法，否则很麻烦
# 协变坐标系
g1 = array([1.3, 0.2])
g2 = array([0.2, 1.5])
co_coord = Coord(ax, g1, g2, "red")
co_coord.draw_basis()

contra_coord = co_coord.get_dual_coord(color="blue")
contra_coord.draw_basis()

# 接下来如何显示向量以及它在不同坐标系下面的分量？
vector = array([2, 3])
draw_vector(ax, vector, with_components=True)
co_coord.draw_components_for_vector(vector)
contra_coord.draw_components_for_vector(vector)

plt.show()

