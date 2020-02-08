from matplotlib.pyplot import show
from numpy import *

from common.cartesian import Cartesian
from common.common import get_column_from_matrix
from common.oblique_coord import ObliqueCoord

'''
验证笛卡尔坐标、逆变坐标、协变坐标、度量张量之间的关系
还不认可逆变、协变坐标和对偶坐标系的概念
'''
ax = Cartesian(-1, 15)
# python有精度损失。

# M的读数是M.T这个坐标系的。不能直接绘制。
M = mat([[2, 0.5],
         [1.5, 2]])

MT = M.T
# 将M的两个基向量的读数转换成笛卡尔读数
M1 = MT @ M
print(M1)
# 现在可以绘制了。已经是笛卡尔读数。注意绘制的并不是M.T，
# 真正的两个基向量还是在M里面表示的，只是他的读数是基于M.T的。M.T又有自己的基向量
ax.draw_vector(get_column_from_matrix(M1, 0), color="red")
ax.draw_vector(get_column_from_matrix(M1, 1), color="red")

ax.draw_vector(get_column_from_matrix(MT, 0), color="green")
ax.draw_vector(get_column_from_matrix(MT, 1), color="green")

# 如果一直M中的一个向量，读数是[1,1], 这个向量的笛卡尔读数是多少？
v = [1, 1]
v_c = M1 @ v
v_c1 = M @ v
ax.draw_vector([v_c[0, 0], v_c[0, 1]], color="blue")
coord = ObliqueCoord(ax, get_column_from_matrix(M, 0), get_column_from_matrix(M, 1), "yellow")
coord.draw_vector(v)
# ax.draw_vector([v_c1[0, 0], v_c1[0, 1]], color="blue")
show()
