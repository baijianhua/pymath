import matplotlib.pyplot as plt
import numpy as np

# 已知x, y, Z
x = np.array([1, 2, 3])
y = np.array([2, 3, 4, 5])
Z = np.random.random((4, 3))

# 建立网格
X, Y = np.meshgrid(x, y)

# 注意X, Y, Z都是大写,赋值a后面要用到
a = plt.contourf(X, Y, Z, 3, cmap=plt.cm.Spectral)

# 赋值b后面要用到
b = plt.contour(X, Y, Z, 3, colors='black', linewidths=1, linestyles='solid')

# 添加colorbar，ticks在这里可省略
plt.colorbar(a, ticks=[0, 0.25, 0.5, 0.75, 1])

# 添加图内标签
plt.clabel(b, inline=True, fontsize=10)
plt.show()
