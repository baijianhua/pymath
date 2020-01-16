from numpy import *
from matplotlib.pyplot import *

from bases.common import get_column_from_matrix
from bases.oblique_coord import ObliqueCoord
from bases.cartesian import Cartesian

M0 = mat([[2, 0],
          [0, 2]])
M1 = mat([[2, 0],
          [0, 2]])
M2 = mat([[2, 0],
          [1, 2]])
v = [1, 1]

vc = M0 @ M1 @ M2 @ v
print(vc)
print(M0.I @ M1.I @ M2.I @ [8, 12])
