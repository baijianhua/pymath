import matplotlib.pyplot as plt
# from common.oblique_coord import ObliqueCoord
# from common.cartesian import Cartesian
from numpy import *

from comm.cartesian import Cartesian
from comm.oblique_coord import ObliqueCoord

cartesian = Cartesian(-2, 6)
# 用numpy的array而非python原生array,来方便做向量与标量的乘法，否则很麻烦
# 协变坐标系
g1 = array([0.6, 0.2])
g2 = array([0.2, 1.7])
co_coord = ObliqueCoord(cartesian, g1, g2, "red")

# 逆变坐标系
contra_coord = co_coord.get_dual_coord(color="blue")
# contra_coord.to_cartesian_components([1, 1])

co_coord.draw_basis()
contra_coord.draw_basis()

# 显示向量以及它在不同坐标系下面的分量
cartesian_vector = array([4, 3])
v1 = co_coord.to_oblique_components(cartesian_vector)
v2 = contra_coord.to_oblique_components(cartesian_vector)
print("笛卡尔读数", cartesian_vector)
print("斜角读数", v1)
print("对偶读数", v2)
print("斜角和对偶点乘", v1@v2)

cartesian.draw_vector(cartesian_vector, with_components=True)
co_coord.draw_oblique_components(cartesian_vector)
contra_coord.draw_oblique_components(cartesian_vector)

plt.show()
