from numpy import *
from matplotlib.pyplot import *

from bases.common import get_column_from_matrix
from bases.oblique_coord import ObliqueCoord
from bases.cartesian import Cartesian
# numpy 不支持这种运算
# m1 = mat([['a', 'b'],
#           ['c', 'd']])
# print(m1)
# print(m1.I)
ax = Cartesian(-5, 12)
# python有精度损失。要靠合理选取数字。不能控制吗？
g1 = array([0.8, 0.2])
g2 = array([1, 3])

co_coord = ObliqueCoord(ax, g1, g2, "red")
co_coord.draw_basis()


g = co_coord.G
gd = co_coord.G_dual
gi = co_coord.G_inverse
m = co_coord.metrics_tensor
print("G", g)
print("G.I", gi)
print("G.dual", gd)
print("G@G.I", g@gi)
print("metrics tensor", co_coord.metrics_tensor)
v = array([3, 4])
v1 = co_coord.to_oblique_components(v)
dual_coord = co_coord.get_dual_coord("blue")
v2 = dual_coord.to_oblique_components(v)
dual_coord.draw_basis()

print("v in cartesian", v)
print("v in oblique", v1)
print("v in dual", v2, m@v1)
print("v1@v2", v1@v2)

ax.draw_vector(v, True)
co_coord.draw_oblique_components(v)
dual_coord.draw_oblique_components(v)
print("v1.T @ m @v1", v1.T @ m @ v1)


coord3 = ObliqueCoord(ax, get_column_from_matrix(gi, 0), get_column_from_matrix(gi, 1), "green")
coord3.draw_basis()
coord4 = ObliqueCoord(ax, get_column_from_matrix(m, 0), get_column_from_matrix(m, 1), "yellow")
coord4.draw_basis()


wm = get_current_fig_manager()
wm.window.geometry("600x600")
show()
