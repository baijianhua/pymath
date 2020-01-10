# https://matplotlib.org/3.1.1/tutorials/toolkits/axisartist.html
import matplotlib.pyplot as plt
from bases.cartesian import init_coord, draw_basis, draw_components, draw_vector, get_column_from_matrix, \
        draw_components_in_coord
from numpy import *

ax = init_coord(-2, 6)
# 用numpy的array而非python原生array,来方便做向量与标量的乘法，否则很麻烦
g1 = array([1.3, 0.2])
g2 = array([0.2, 1.5])
# 协变分量的两个基向量为列构成的矩阵,要转置一下，否则方向不对
G = mat([g1, g2]).T
print(G)
# 逆变坐标系, 要是直接能用1/g1得出rg1就好了。这是不行的，不仅要g1*rg1=1, 还要g1*rg2=0
G1 = G.I
print(G1)
rg1 = array(get_column_from_matrix(G1, 0))
rg2 = array(get_column_from_matrix(G1, 1))
print(rg1*3)
print(rg2*3)

draw_basis(ax, G, "red")
draw_basis(ax, G1, "blue")

# 接下来如何显示向量以及它在不同坐标系下面的分量？
vector = array([2, 3])
draw_vector(ax, vector, with_components=True)
draw_components_in_coord(ax, vector, G, color="red")
draw_components_in_coord(ax, vector, G1, color="blue")

plt.show()

