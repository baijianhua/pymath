import numpy as np
import matplotlib.pyplot as plt

# 1.圆半径
r = 2.0
# 2.圆心坐标
a, b = (0., 0.)
# 参数方程
theta = np.arange(0, 2*np.pi, 0.01)
x = a + r * np.cos(theta)
y = b + r * np.sin(theta)
# 绘图
fig = plt.figure()
axes = fig.add_subplot(111)

axes.plot(x, y)
axes.axis('equal')

plt.axhline(linewidth=2, color='r')
plt.axvline(linewidth=2, color='r')
plt.show()
