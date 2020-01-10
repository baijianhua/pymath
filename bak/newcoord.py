import matplotlib.pyplot as plt
import numpy as np
from matplotlib.axes import Axes
from matplotlib.figure import Figure

from bak.basic_units import cm

x = np.linspace(0, 20, 2)
cm_x = [i * cm for i in x]
fig: Figure
ax: Axes
fig, ax = plt.subplots()
ax.plot(cm_x, cm_x, ls="-", lw=3, color="k", xunits=cm, yunits=cm)
ax.set_ylabel("")
ax.set_xlabel("")

plt.show()


z = 10
print(z)
z = "abc"
print(z)

