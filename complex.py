from numpy import *
import matplotlib.pyplot as plt


def plot_complex(start_x, start_y, end_x, end_y, step):
    for yy in arange(start_y, end_y, step):
        xx = arange(start_x, end_x, step)
        plt.plot(xx, yy)


plot_complex(2, 2, 5, 5, 0.1)
plt.show()
