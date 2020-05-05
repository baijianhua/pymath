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

这是从原点出发的一个向量啊。

而且有个问题理解不了。是不是任何曲线坐标系，一定要和笛卡尔坐标系相关？那么拉伸的平面作何解释？
球面几何、曲面几何，尚可通过嵌入到三维空间（虽然它本身只有 u,v 两个维度，但x,y,z分别是u,v的函数，或者说u,v是x,y,z的函数）
但变形的二维空间无法嵌入三维空间，弯曲和变形是不同的。

更何况广义相对论只是在讨论思维变形，从来没有去嵌入到更高维度的空间。

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
