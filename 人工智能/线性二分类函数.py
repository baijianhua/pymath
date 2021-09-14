# from math import e
from math import e

from sympy import symbols, print_latex
from matplotlib import pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

plt.figure()
ax = plt.axes(projection="3d")
MAX = 10
MIN = -10

w1 = 1
w2 = 2

b = 0
x = np.arange(MIN, MAX, 0.5)
y = np.arange(MIN, MAX, 0.5)
X, Y = np.meshgrid(x, y)  # 2生成绘制3D图形所需的网络数据
Z = x * w1 + Y * w2 + b
Z1 = 5 / (1 + e ** (-Z))

ax.plot_surface(X, Y, Z, alpha=0.5, cmap="winter")
ax.plot_surface(X, Y, Z1, alpha=0.7, cmap="rainbow")

ax.scatter(0, 0, 0, c='r', marker='o')
# 生成表面，alpha用于控制透明度
# ax.contour(X,Y,Z,zdir="x",offset=-6,cmap="rainbow")   #x轴投影
# ax.contour(X,Y,Z,zdir="y",offset=6,cmap="rainbow")    #y轴投影
# ax.contour(X,Y,Z,zdir="z",offset=-3,cmap="rainbow")   #z轴投影
ax.set_xlabel("X")  # 设置X、Y、Z 坐标范围
ax.set_xlim(MIN, MAX)  # 设置X、Y、Z 轴
ax.set_ylabel("Y")
ax.set_ylim(MIN, MAX)
ax.set_zlabel("Z")
plt.show()

