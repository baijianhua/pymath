"""
将复变函数（向量函数）在平面画出来
"""

# 没这句不行，利用了里面的Axes.ms_init = ms_init
from sympy import E

from common import *
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.axes import Axes


def f(x, y): return E ** (x + y)


def f1(x): return E ** x


ax: Axes = plt.gca()
ax.grid(True)
# ax.ms_init(min_size, max_size)
# 定义起点终点和步长
x = np.arange(-0.2, 2, 0.1)
# 把y值画在x轴上，实现一维映射
x1 = [f1(i) for i in x]
y1 = [0 for i in x]
ax.scatter(x1, y1)
plt.show()
