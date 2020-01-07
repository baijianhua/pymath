#用python绘制坐标
#https://matplotlib.org/examples/axes_grid/demo_axisline_style.html
#https://stackoverflow.com/questions/13430231/how-i-can-get-cartesian-coordinate-system-in-matplotlib
#https://stackoverflow.com/questions/50798265/what-is-subplotzero-documentation-lacking

# notice import as 和 from import有什么区别？
import numpy as np
import matplotlib.pyplot as plt

from matplotlib.axes import Axes
from matplotlib.figure import Figure
from basic_units import cm

fig: Figure = plt.figure()
# notice 得到并设置坐标坐标系
ax: Axes = fig.subplots()
ax.set_title('x axis spine at zero data coordinate')
ax.set_xlabel("Axes zero")
ax.set_ylabel("Y")
ax.axis()
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.set_xlim(-3, 10)
ax.set_ylim(-3, 10)

# todo 设定坐标轴的样式和刻度
yAxis: Axes = ax.spines['left']
yAxis.set_position(('data', 0))
xAxis: Axes = ax.spines['bottom']
xAxis.set_position(('data', 0))
xAxis.set_axisline_style("-|>")

# notice 设定x的范围
x = np.arange(-1, 3, 0.01)
# notice 绘制图形
ax.plot(x, 2*x, xunits=cm, yunits=cm)

plt.show()
