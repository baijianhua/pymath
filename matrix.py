from numpy import *
from matplotlib.pyplot import *
from bases.oblique_coord import ObliqueCoord
from bases.cartesian import Cartesian

# m1 = mat([['a', 'b'],
#           ['c', 'd']])
# print(m1)
# print(m1.I)


ax = Cartesian(-2, 6)
g1 = array([3, 1])
g2 = array([1, 4])

co_coord = ObliqueCoord(ax, g1, g2, "red")
co_coord.draw_basis()


print(co_coord.G)


#show()

