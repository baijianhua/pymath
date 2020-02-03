# 没这句不行，利用了里面的Axes.ms_init = ms_init
from common import *
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.axes import Axes


min_size = -5
max_size = 20
fig, ax1 = plt.subplots(1, 1)
ax: Axes = ax1
xx, yy = np.linspace(min_size, max_size), np.linspace(min_size, max_size)
# 采样点，这样得到一个平面区域，这个采样点的密度是多少呢？
x, y = np.meshgrid(xx, yy)
# 扩展方法
ax.ms_init(min_size, max_size)
# 怎样才能再把x,y绘制回去？
ax.plot()
plt.show()
