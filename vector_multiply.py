from matplotlib.pyplot import show
from numpy import *

from bases.cartesian import Cartesian
from bases.oblique_coord import ObliqueCoord

a = array([5, 1])
b = array([2, 6])
cartesian = Cartesian(-2, 15)
oblique = ObliqueCoord(cartesian, a, b, "red")
oblique.draw_basis()

print("[a,b].T")
print(oblique.G)

print("\n坐标乘, 结果是向量")
print(multiply(a, b))
print(a * b)

print("\n內积，点乘，矩阵乘，结果是标量")
print(dot(a, b))
print(inner(a, b))
print(a @ b)

print("\n叉积，向量乘，结果是向量，但只有一个长度读数。方向是垂直于a,b")
print(cross(a, b))

print("\n外积，并矢，张量乘，结果是矩阵，张量")
print(outer(a, b))

print("\n度量张量")
print(oblique.metrics_tensor)
show()
