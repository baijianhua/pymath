from numpy import *
from common.orthogonalcoord import OrthogonalCoord
from common.oblique_coord import ObliqueCoord
import matplotlib.pyplot as plt

'''
验证笛卡尔坐标、逆变坐标、协变坐标、度量张量之间的关系
还不认可逆变、协变坐标和对偶坐标系的概念
'''
max = 5
lspace = 50

ax = OrthogonalCoord(-1, max)
# python有精度损失。
v = 0.8
gamma = 1/sqrt(1-v**2)
# 为什么这里是v而不是洛伦兹变换矩阵里面的-v? 因为这是逆变换？
g1 = array([1, v])*gamma
g2 = array([v, 1])*gamma
co_coord = ObliqueCoord(ax, g1, g2, "red")
co_coord.draw_basis()
co_coord.draw_vector([1, 1], draw_components=True)
# co_coord.draw_oblique_components()

# 绘制双曲线
xlist = linspace(-2, max, lspace)
ylist = linspace(-2, max, lspace)
X, Y = meshgrid(xlist, ylist)

F = X**2 - Y**2 - 1
plt.contour(X, Y, F, [0], colors='b', linestyles='dashed', linewidths=1)

F = Y**2 - X**2 - 1
plt.contour(X, Y, F, [0], colors='b', linestyles='dashed', linewidths=1)

plt.show()
