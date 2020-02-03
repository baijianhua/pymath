# 没这句不行，利用了里面的Axes.ms_init = ms_init
from common import *
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.axes import Axes


def f(x): return x ** 2


min_size = -5
max_size = 20
ax: Axes = plt.gca()
ax.grid(True)
# ax.ms_init(min_size, max_size)
# 定义起点终点和步长
x = range(-3, 15, 1)
# 把y值画在x轴上，实现一维映射
x1 = [f(i) for i in x]
y1 = [0 for i in x]
ax.scatter(x1, y1)
plt.show()
