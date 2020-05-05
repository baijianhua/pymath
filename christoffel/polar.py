"""
Demo of a line plot on a polar axis.

https://www.youtube.com/watch?v=3CjdFR5f1ew
"""
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.axes import Axes

from sympy import *
from sympy.diffgeom import *

erhohat = symbols('ehat')
rho, phi = symbols('rho, phi')
x, y = symbols('x, y')

"""
如果以极坐标的rho和phi为自变量，如何求(rho_0, phi_0)一点的笛卡尔坐标中x,y的值
"""
fx = rho * cos(phi)
fy = rho * sin(phi)
# r stands for vector in rho and phi,
# this is a r in a local coordinate system.


"""
如何用rho和phi来表示一个向量，用+号让我觉得不舒服，这两部分之间其实是没关系的。
这是采用复数的方式？

这本质上还是在用笛卡尔坐标在表示向量。

这是从原点出发的一个向量啊。不过刚巧极坐标中所有的向量都可以用这个方式表达。所以这个函数式是全局通用的。
可能所有这些问题，
***都还是脱离不了笛卡尔坐标系***
即使没有一个通用公式，起码也要有局部的转换函数。

有了这个到笛卡尔坐标系的转换函数（点对点转换，和向量无关）。就可以针对这个坐标系的变量求偏导数。 
不论这个转换函数是全局的，还是局部的，求偏导数得到的两个向量（即协变基矢量），都可以作为一个局部坐标系。
这个转换函数，对谁求偏导数，就是沿着谁的方向的一个向量。而且方向这个词都不一定对。比如极坐标中
r和theta, 只能说顺着变量(r,theta)的增减方向变化。不过变量如果可以绘制在图形上，那总是有个趋势的。

在这个得到的局部坐标系中的的向量（多半以这个局部坐标系的原点为起点），可以表示为相对于这两个向量的分量。

联络系数（Christoffel Symbol）就是为了解决如何比较向量的问题，两个向量处在两个局部坐标系中，分别用
各自的基向量表示。为了进行比较，要把以A对儿基向量表示的向量转换为通过B对儿基向量表示。

在A中，向量的表达式是 

而且有个问题理解不了。是不是任何曲线坐标系，一定要和笛卡尔坐标系相关？那么拉伸的平面作何解释？
球面几何、曲面几何，尚可通过嵌入到三维空间（虽然它本身只有 u,v 两个维度，但x,y,z分别是u,v的函数，或者说u,v是x,y,z的函数）
但变形的二维空间无法嵌入三维空间，弯曲和变形是不同的。

更何况广义相对论只是在讨论四维变形，从来没有去嵌入到更高维度的空间。

那这样说，局部坐标系到底是怎么来的？

应该是没有笛卡尔坐标系这个东西的吧？在四维空间中，如果有，1这个数字怎么定义？一个单位距离，或者说一个单位时间，到底是多少？
"""
r = rho * cos(phi) + rho * sin(phi)
# erho = symbols('e_rho')
"""
下面这个计算的结果是，是协变基矢量中的e_rho。
"""
ferho = diff(r, rho)
pprint(ferho)
print_latex(ferho)
print("计算erho的模长")
pprint(sqrt(ferho*ferho))
fephi = diff(r, phi)
pprint(sqrt(ferho*ferho))







print_latex(fephi)

# dyphi = diff(fy, phi)
# dxphi = diff(fx, phi)
#
# dxrho = diff(fx, rho)
# dyrho = diff(fy, rho)

# pprint(dxrho)
# pprint(dyrho)
#
# pprint(dxphi)
# pprint(dyphi)
#
# pprint(diff(dxphi, phi, evaluate=False))
# pprint(diff(dyphi, phi))
