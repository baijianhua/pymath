# https://matplotlib.org/3.1.1/tutorials/toolkits/axisartist.html
import matplotlib.pyplot as plt
from bases.cartesian import init_coord, draw_basis
from numpy import *

ax = init_coord(-2, 6)
g1 = [1, 4]
g2 = [2, 1]

# 协变分量的两个基向量为列构成的矩阵
G = mat([g1, g2]).T
print(G)
# 逆变坐标系
G1 = G.I
print(G1)

# 以第一列为起点，第二列为终点, 第三个参数是颜色
# linestyle='dashed'

ax.plot([0, g1[0]],
        [0, g1[1]],
        color="red"
        )

ax.plot([0, g2[0]],
        [0, g2[1]],
        color="red"
        )

draw_basis(ax, G1, "blue")
# print(G1[0, 0])
plt.show()

