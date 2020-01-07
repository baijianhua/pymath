# https://matplotlib.org/3.1.1/tutorials/toolkits/axisartist.html
from mpl_toolkits.axisartist import AxisArtist
from mpl_toolkits.axisartist.axislines import SubplotZero, Axes
import matplotlib.pyplot as plt
import numpy as np

from mpl_toolkits.axisartist.grid_helper_curvelinear import GridHelperCurveLinear
from mpl_toolkits.axisartist import Subplot

fig = plt.figure(figsize=(12, 12))
ax: Axes = SubplotZero(fig, 111)
ax.set_xlim(-2, 10)
ax.set_ylim(-2, 10)
#ax.set_xticks([-2,1,0,1,10])

ticks = [i for i in range(-2, 10) if i != 0]

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

# # from curved coordinate to rectlinear coordinate.
# def tr(x, y):
#     x, y = np.asarray(x), np.asarray(y)
#     return x, y-x
#
# # from rectlinear coordinate to curved coordinate.
# def inv_tr(x,y):
#     x, y = np.asarray(x), np.asarray(y)
#     return x, y+x
#
# grid_helper = GridHelperCurveLinear((tr, inv_tr))
# ax1 = Subplot(fig, 1, 1, 1, grid_helper=grid_helper)
#
# fig.add_subplot(ax1)

plt.show()

