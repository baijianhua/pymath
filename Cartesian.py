from mpl_toolkits.axes_grid.axislines import SubplotZero
from matplotlib.transforms import BlendedGenericTransform
import matplotlib.pyplot as plt
import numpy

fig = plt.figure(1)
ax = SubplotZero(fig, 111)
fig.add_subplot(ax)

ax.axhline(linewidth=2.0, color="black")
ax.axvline(linewidth=2.0, color="black")

ax.set_xticks([])
ax.set_yticks([])

ax.text(0, 1.05, 'y', transform=BlendedGenericTransform(ax.transData, ax.transAxes), ha='center')
ax.text(1.05, 0, 'x', transform=BlendedGenericTransform(ax.transAxes, ax.transData), va='center')

for direction in ["xzero", "yzero"]:
    ax.axis[direction].set_axisline_style("-|>")
    ax.axis[direction].set_visible(True)

for direction in ["left", "right", "bottom", "top"]:
    ax.axis[direction].set_visible(False)

x = numpy.linspace(-0.5, 1., 100)
ax.plot(x, numpy.sin(x*numpy.pi), linewidth=2.0)

plt.show()
