import matplotlib.pyplot as plt
from matplotlib.axes import Axes


def draw_vector(x, y, to_x, to_y):
    plt.quiver(x, y, to_x, to_y, angles='xy', scale_units='xy', scale=1, color='#FF0000')


plt.xlabel('x')
plt.ylabel('y')
plt.title('Coordinate')
plt.grid(True)

draw_vector(0, 0, 4, 5)
# 获取当前坐标轴, 并调整当前坐标的特点
axes: Axes = plt.gca()
axes.set_aspect('equal')
axes.set_xlim(-2, 10)
axes.set_ylim(-2, 10)

plt.show()
