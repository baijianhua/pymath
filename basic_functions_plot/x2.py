from numpy import *
import matplotlib.pyplot as plt

x = arange(-5, 5, .01)
y = x ** 2

plt.plot(x, y)
# draw a thick red hline at y=0 that spans the xrange
plt.axhline(linewidth=2, color='r')
plt.axvline(linewidth=2, color='r')
# plt.axis([-1, 2, -1, 2])

plt.show()
