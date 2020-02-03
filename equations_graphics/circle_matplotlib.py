import matplotlib.pyplot as plt
import numpy as np
from matplotlib.axes import Axes

fig, ax1 = plt.subplots(1, 1)
ax: Axes = ax1
xx, yy = np.linspace(-3, 10), np.linspace(-3, 10)
x, y = np.meshgrid(xx, yy)
ax.contour(x, y, ((x-2) ** 2 + (y-3) ** 2 - 9), [0])
# ax.plot([0], [0], "o")
# ax.plot(xx, yy)
ax.axhline()
ax.axvline()
ax.set_aspect('equal')
ax.grid(True)
plt.show()
