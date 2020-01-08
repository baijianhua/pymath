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

# 已知笛卡尔坐标，求斜角坐标，可以考虑用向量与两个基向量点乘，再分别除以基向量的模长。这样能得到斜角坐标读数
# 总感觉向量点乘、转置、逆矩阵这些东西之间有几何联系

# 向量的点乘是投影，这是很有意思的结论，为什么？是一个代数偶然吗？

# 矩阵乘以向量，等于将向量变形，或者说，将斜角坐标翻译成笛卡尔坐标，这个应该有个漂亮的几何解释才对
# 为什么是用两个基向量的横坐标乘以向量，得到新向量的横坐标读数，再用基向量的y读数，乘以向量，得到新向量的y读数?

draw_vector(0,0,6,6)
# axes: Axes = plt.axes(label="axes1")
# 获取当前坐标轴
axes: Axes = plt.gca()
axes.set_aspect('equal')
axes.set_xlim(-5, 20)
axes.set_ylim(-5, 20)

plt.show()
