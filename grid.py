import matplotlib.pyplot as plt
from pyplot_ext import draw_vector
from matplotlib.axes import Axes


# x = np.arange(0.0, 1.0 + 0.01, 0.01)
# y = 2*x
# plt.plot(x, y, '-', lw=2)

plt.xlabel('x')
plt.ylabel('y')
plt.title('Coordinate')
plt.grid(True)

draw_vector(0,0,1,5)
draw_vector(0, 0, 4, 0.5)
# axes: Axes = plt.axes(label="axes1")
# 获取当前坐标轴
axes: Axes = plt.gca()
axes.set_aspect('equal')
axes.set_xlim(-2, 10)
axes.set_ylim(-2, 10)

plt.show()
