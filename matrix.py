from numpy import *
from matplotlib.pyplot import *

from bases.common import get_column_from_matrix
from bases.oblique_coord import ObliqueCoord
from bases.cartesian import Cartesian

ax = Cartesian(-3, 7)
# python有精度损失。
g1 = array([0.8, 0.3])
g2 = array([0.1, 1.1])

co_coord = ObliqueCoord(ax, g1, g2, "red")
dual_coord = co_coord.get_dual_coord("blue")
co_coord.draw_basis()
dual_coord.draw_basis()

g = co_coord.G
gd = co_coord.G_dual
gi = co_coord.G_inverse
m = co_coord.metrics_tensor
print("G", g)
print("G.I", gi)
print("G.dual", gd)
print("G@G.I", g @ gi)
print("metrics tensor", co_coord.metrics_tensor)


v_c = array([2, 3])
v_o = co_coord.to_oblique_components(v_c)
v_d = dual_coord.to_oblique_components(v_c)

print("v in cartesian", v_c)
print("v in oblique", v_o)
print("v in dual", v_d, m @ v_o, gd.I @ v_c)
print("v_o@v_d", v_o @ v_d)

ax.draw_vector(v_c, True)
co_coord.draw_oblique_components(v_c)
dual_coord.draw_oblique_components(v_c)
print("v1.T @ m @v1", v_o.T @ m @ v_o)


wm = get_current_fig_manager()
if hasattr(wm, 'window'):
    wm.window.geometry("600x600")

show()
