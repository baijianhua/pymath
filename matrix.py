from numpy import *
from matplotlib.pyplot import *
from bases.oblique_coord import ObliqueCoord
from bases.cartesian import Cartesian
# numpy 不支持这种运算
# m1 = mat([['a', 'b'],
#           ['c', 'd']])
# print(m1)
# print(m1.I)
ax = Cartesian(-4, 8)
g1 = array([4, 2])
g2 = array([1, 4])

co_coord = ObliqueCoord(ax, g1, g2, "red")
co_coord.draw_basis()


g = co_coord.G
gd = co_coord.G_dual
gi = co_coord.G_inverse
print("G", g)
print("G.I", gi)
print("G.dual", gd)
print("G@G.I", g@gi)
print("metrics tensor", co_coord.metrics_tensor)
v = array([3, 4])
v1 = co_coord.to_oblique_components(v)
print("v in oblique", v1)
dual_coord = co_coord.get_dual_coord("blue")
v2 = dual_coord.to_oblique_components(v)
dual_coord.draw_basis()
print("v in dual", v2)
print("v1@v2", v1@v2)

ax.draw_vector(v, True)
co_coord.draw_oblique_components(v)
dual_coord.draw_oblique_components(v)
m = co_coord.metrics_tensor
print("v1.T @ m @v1", v1.T @ m @ v1)

show()

