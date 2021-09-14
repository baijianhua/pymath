# 载入模块
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
# import pandas as pd
import seaborn as sns
from scipy import interpolate


#生成数据
x = np.linspace(0.1,0.9,9)
y = np.linspace(0.1,0.9,9)
z = np.random.rand(81)

#插值
# xx, yy = np.meshgrid(x, y)

f = interpolate.interp2d(x, y, z, kind='cubic')
xnew = np.arange(0.1, 1, 0.03)
ynew = np.arange(0.1, 1, 0.03)
znew = f(xnew, ynew)

#修改x,y，z输入画图函数前的shape
xx1, yy1 = np.meshgrid(xnew, ynew)
newshape = (xx1.shape[0])*(xx1.shape[0])
y_input = xx1.reshape(newshape)
x_input = yy1.reshape(newshape)
z_input = znew.reshape(newshape)
znew1 = f(x_input, y_input)
#画图
# sns.set(style='white')
fig = plt.figure()
# ax = fig.add_subplot(111, projection='3d')
# ax.plot_trisurf(x_input,y_input,z_input,cmap=cm.coolwarm)
plt.contour(x_input, y_input, znew1, 8, alpha=.75, cmap=plt.cm.jet)


plt.show()
