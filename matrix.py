from numpy import *
from matplotlib.pyplot import *
from bases.cartesian import Cartesian, Coord

ax = Cartesian(-2, 6)
g1 = array([3, 1])
g2 = array([1, 4])

co_coord = Coord(ax, g1, g2, "red")
co_coord.draw_basis()


print(co_coord.G)


show()

