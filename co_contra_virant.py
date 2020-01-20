from numpy import *

from bases.cartesian import Cartesian
from bases.oblique_coord import ObliqueCoord

'''
验证笛卡尔坐标、逆变坐标、协变坐标、度量张量之间的关系
还不认可逆变、协变坐标和对偶坐标系的概念
'''
ax = Cartesian(-3, 7)
# python有精度损失。
g1 = array([0.8, 0.3])
g2 = array([0.1, 1.1])
co_coord = ObliqueCoord(ax, g1, g2, "red")
contra_coord = co_coord.get_dual_coord("blue")

g = co_coord.G
gt = co_coord.G.T
gd = co_coord.G_dual
gi = co_coord.G_inverse
m = co_coord.metrics_tensor

v_c = array([2, 3])
v_o = co_coord.to_oblique_components(v_c)
v_d = contra_coord.to_oblique_components(v_c)

print("G", g)
print("G.I", gi)
print("G.dual", gd)
print("metrics tensor", co_coord.metrics_tensor)
print("v in cartesian", v_c)
print("v in oblique", v_o)
print("v_o to cartesian", co_coord.to_cartesian_components(v_o))
print("v in dual", v_d, m @ v_o, gd.I @ v_c)
print("v_o@v_d", v_o @ v_d)
print("gd.T @ v_c == v_o?", gd.T @ v_c)
# G.dual.T @ v_c = v_o, 但是G.dual @ v_c 可不等于v_o.T!!!
# print("gd @ v_c == v_o.T?", gd @ v_c)
print("v_c @ dual_coord.G", v_c @ contra_coord.G)
print("v1.T @ m @v1", v_o.T @ m @ v_o)

print(v_d @ v_o, v_c @ v_c)
print(g @ v_o)
print(v_d @ g.T.I)

