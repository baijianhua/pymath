import numpy as np

"""
meshgrid的结果，
第一个是横坐标轴的数据的集合
第二个是纵坐标轴数据的集合
两者合起来构成一个网格点的集合

x[0]与y[0] 逐个元素组合，是四个点的坐标，这些点构成一条横线。纵坐标是y[i], 横坐标是x[i]
"""
grid_x, grid_y = np.meshgrid(np.linspace(-3, 3, 4), np.linspace(-3, 3, 4))
print(grid_x)
print("-----------------")
print(grid_y)