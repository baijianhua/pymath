"""
如果度量张量是投影，那并矢是什么？


绘制度一个向量的笛卡尔坐标、斜角坐标以及对偶坐标

再次声明，对偶坐标，逆变、协变分量，这些概念，只是借用一下而已。
不完全认同，而且这些概念本身可能有错误。
"""
from numpy import *
from matplotlib.pyplot import *

from common.oblique_coord import ObliqueCoord
from common.orthogonalcoord import OrthogonalCoord

ax = OrthogonalCoord(-3, 7, show_grid=False)

# python有精度损失。
g1 = array([0.5, 2])
g2 = array([1.7, 0.3])


co_coord = ObliqueCoord(ax, g1, g2, "red")
dual_coord = co_coord.get_dual_coord("blue")
co_coord.draw_basis()
dual_coord.draw_basis()

v_c = array([2, 3])
v_o = co_coord.to_oblique_components(v_c)
v_d = dual_coord.to_oblique_components(v_c)

ax.draw_vector(v_c, True)
co_coord.draw_oblique_components(v_c)
dual_coord.draw_oblique_components(v_c)

show()
