#用python绘制坐标
#https://matplotlib.org/examples/axes_grid/demo_axisline_style.html
#https://stackoverflow.com/questions/13430231/how-i-can-get-cartesian-coordinate-system-in-matplotlib

from mpl_toolkits.axisartist import SubplotZero
import matplotlib.pyplot as plt
import numpy as np


fig = plt.figure(1)
# 把画布分成1行1列，把元素放在第一个格子
ax = SubplotZero(fig, 111)
fig.add_subplot(ax)

for direction in ["xzero", "yzero"]:
    ax.axis[direction].set_axisline_style("-|>")
    ax.axis[direction].set_visible(True)


for direction in ["left", "right", "bottom", "top"]:
    ax.axis[direction].set_visible(False)


x = np.linspace(-10, 10, 100)
ax.plot(x, 2*x)


# ax1 = SubplotZero(fig, 221)
# fig.add_subplot(ax1)

plt.show()
