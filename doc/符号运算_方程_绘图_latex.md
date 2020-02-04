# 好例子
http://www.faculty.umassd.edu/j.wang/vp/  
http://elektromagnetisme.no/category/fys1120/tips-tricks/  
# Latex
# 偏微分
现在把具体方程放在偏微分符号右边，看起来还是怪怪的。应该用一个f来代替才对吧？而且这个f应该写在分子上才好

# 方程及其绘制
## 用sympy绘制方程
强大到让人汗颜......  
https://docs.sympy.org/1.5.1/modules/plotting.html 
```python
from sympy import *
x, y = symbols('x y')
eq = Eq(x**2 + y**2, 9)
plot_implicit(eq)

```
指定范围
```
p2 = plot_implicit(Eq(x**2 + y**2, 3),
        (x, -3, 3), (y, -3, 3))
```

但这个有个问题，不能指定坐标轴的纵横比，会变形。  
需要自己有点黑客手段。

```
def plot_equation(eq: Equality, x_var=None, y_var=None,):
    # 创建plot但不绘制
    plot = plot_implicit(eq, x_var, y_var, show=False)
    # 自己初始化一个绘制引擎
    matplot = MatplotlibBackend(plot)
    # backend 给每个plot创建一个单独的坐标系，所以要取出坐标系来单独设置
    ax: Axes = matplot.ax[0]
    ax.set_aspect('equal')
    ax.grid(True)
    matplot.show()
```

## 用matlablib 绘制方程
其实这个也挺好用的。这有几个优点
- 把坐标刻度绘制在左边和下边其实比绘制在x,y轴上面好看。
- 绘制控制更灵活，线的颜色、粗细等等
```python
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.axes import Axes

fig, ax1 = plt.subplots(1, 1)
ax: Axes = ax1
xx, yy = np.linspace(-3, 3), np.linspace(-3, 3)
x, y = np.meshgrid(xx, yy)
ax.contour(x, y, (x ** 2 + y ** 2 - 4), [0])
#ax.plot([0], [0], "o")
# ax.plot(xx, yy)
ax.axhline()
ax.axvline()
ax.set_aspect('equal', 'datalim')
ax.grid(True)
plt.show()
```
# 带入常数
https://pythonforundergradengineers.com/sympy-expressions-and-equations.html

## sympy上下标
变量名和符号内容不需要一致。符号内容在打印的时候才需要。

```python
from sympy import *
x, y, z1 = symbols('x_{1}^2 y z1')
expr1 = exp(x*y*z1)
r2 = latex(diff(expr1, x, evaluate=False))
```

## 绘制矢量场
https://tonysyu.github.io/plotting-streamlines-with-matplotlib-and-sympy.html#.XifWcGgzYSE


# python 3d绘图
https://zhuanlan.zhihu.com/p/74923962
