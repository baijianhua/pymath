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
# 绘制一个向量，并且绘制它到它的基向量、对偶基向量的平行四边形分解
# 求一个向量在某个对偶坐标系的分量其实也容易，只要用这个向量与基向量点乘应该就可以了。
draw_vector(0,0,6,6)
# axes: Axes = plt.axes(label="axes1")
# 获取当前坐标轴
axes: Axes = plt.gca()
axes.set_aspect('equal')
axes.set_xlim(-5, 20)
axes.set_ylim(-5, 20)

plt.show()
