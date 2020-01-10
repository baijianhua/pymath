import matplotlib.pyplot as plt
import mpl_toolkits.axes_grid1.inset_locator as il

fig, (ax1, ax2) = plt.subplots(nrows=2, figsize=(4,4))
ax1.plot([1,2,3],[2.2,2,3])

# set the inset at upper left (loc=2) with width, height=0.5,0.4
axins = il.inset_axes(ax1, "50%", "40%", loc=2, borderpad=1)
axins.scatter([1,2,3],[3,2,3])

# set the inset at 0.2,0.5, with width, height=0.8,0.4
#   in parent axes coordinates
axins2 = il.inset_axes(ax2, "100%", "100%", loc=3, borderpad=0,
    bbox_to_anchor=(0.2,0.5,0.7,0.4),bbox_transform=ax2.transAxes,)
axins2.scatter([1,2,3],[3,2,3])

plt.show()
