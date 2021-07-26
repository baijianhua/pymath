# https://zhuanlan.zhihu.com/p/66306575

from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

plt.figure()
ax = plt.axes(projection="3d")

x = np.arange(-5, 5, 0.1)
y = np.arange(-5, 5, 0.1)
X, Y = np.meshgrid(x, y)  # 2生成绘制3D图形所需的网络数据
Z = X ** 2 + Y ** 2

ax.plot_surface(X, Y, Z, alpha=0.5, cmap="winter")
ax.scatter(0, 0, 0, c='r', marker='o')
# 生成表面，alpha用于控制透明度
# ax.contour(X,Y,Z,zdir="x",offset=-6,cmap="rainbow")   #x轴投影
# ax.contour(X,Y,Z,zdir="y",offset=6,cmap="rainbow")    #y轴投影
# ax.contour(X,Y,Z,zdir="z",offset=-3,cmap="rainbow")   #z轴投影
ax.set_xlabel("X")  # 设置X、Y、Z 坐标范围
ax.set_xlim(-6, 6)  # 设置X、Y、Z 轴
ax.set_ylabel("Y")
ax.set_ylim(-6, 6)
ax.set_zlabel("Z")
plt.show()
