# https://matplotlib.org/3.1.1/tutorials/toolkits/axisartist.html
from mpl_toolkits.axisartist import AxisArtist
from mpl_toolkits.axisartist.axislines import SubplotZero, Axes
import matplotlib.pyplot as plt
import numpy as np

from mpl_toolkits.axisartist.grid_helper_curvelinear import GridHelperCurveLinear
from mpl_toolkits.axisartist import Subplot

img_size = 5
negative = -2
fig = plt.figure(figsize=(img_size - negative, img_size - negative))
ax: Axes = SubplotZero(fig, 111)
ax.set_xlim(negative, img_size)
ax.set_ylim(negative, img_size)
#ax.set_xticks([-2,1,0,1,10])

ticks = [i for i in range(negative, img_size) if i != 0]

ax.set_xticks(ticks)
ax.set_yticks(ticks)
fig.add_subplot(ax)

for direction in ["xzero", "yzero"]:
    # adds arrows at the ends of each axis
    axis: AxisArtist = ax.axis[direction]
    axis.set_axisline_style("-|>")
    axis.set_visible(True)



for direction in ["left", "right", "bottom", "top"]:
    # hides borders
    ax.axis[direction].set_visible(False)

x = np.linspace(0, 2, 100)
ax.plot(x, 2*x)


plt.show()

