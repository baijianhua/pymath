# https://blog.csdn.net/shangboerds/article/details/112598802

import numpy as np
import matplotlib.pyplot as plt


# 根据 x y 坐标返回 z 坐标
def z(x, y):
    return (1 - x / 2 + x ** 5 + y ** 3) * np.exp(-x ** 2 - y ** 2)


n = 256
x = np.linspace(-3, 3, n)
y = np.linspace(-3, 3, n)

# 二维网格坐标
X, Y = np.meshgrid(x, y)
Z = z(X, Y);

# 填充轮廓
plt.contourf(X, Y, Z, 8, alpha=.75, cmap=plt.cm.jet)

# 绘制轮廓线
C = plt.contour(X, Y, Z, 8, colors='black')
plt.clabel(C)

plt.xticks(())
plt.yticks(())
plt.show()
