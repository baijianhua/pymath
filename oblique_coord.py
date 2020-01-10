"""
Custom grid and ticklines.

This example demonstrates how to use GridHelperCurveLinear to define
custom grids and ticklines by applying a transformation on the grid.
This can be used, as showcase on the second plot, to create polar
projections in a rectangular box.
"""

import numpy as np

import matplotlib.pyplot as plt
import matplotlib.cbook as cbook

from mpl_toolkits.axisartist import Subplot
from mpl_toolkits.axisartist import SubplotHost, \
    ParasiteAxesAuxTrans
from mpl_toolkits.axisartist.grid_helper_curvelinear import \
    GridHelperCurveLinear


def curvelinear_test1(fig):
    """
    grid for custom transform.
    """

    def tr(x, y):
        x, y = np.asarray(x), np.asarray(y)
        return x, y - x

    def inv_tr(x, y):
        x, y = np.asarray(x), np.asarray(y)
        return x, y + x

    grid_helper = GridHelperCurveLinear((tr, inv_tr))

    ax1 = Subplot(fig, 1, 1, 1, grid_helper=grid_helper)
    # ax1 will have a ticks and gridlines defined by the given
    # transform (+ transData of the Axes). Note that the transform of
    # the Axes itself (i.e., transData) is not affected by the given
    # transform.

    fig.add_subplot(ax1)

    xx, yy = tr([3, 6], [5.0, 10.])
    ax1.plot(xx, yy, linewidth=2.0)

    ax1.set_aspect(1.)
    ax1.set_xlim(0, 10.)
    ax1.set_ylim(0, 10.)

    ax1.axis["t"] = ax1.new_floating_axis(0, 3.)
    ax1.axis["t2"] = ax1.new_floating_axis(1, 7.)
    ax1.grid(True, zorder=0)


fig = plt.figure(1, figsize=(7, 4))
fig.clf()
curvelinear_test1(fig)
plt.draw()
plt.show()
