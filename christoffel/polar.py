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
"""
如何用rho和phi来表示一个向量，用+号让我觉得不舒服，这两部分之间其实是没关系的。
这是采用复数的方式？


极坐标很奇葩，极坐标其实可以是平直的，但用极坐标表示的向量平移却很麻烦。

在这个得到的局部坐标系中的的向量（多半以这个局部坐标系的原点为起点），可以表示为相对于这两个向量的分量。

联络系数（Christoffel Symbol）就是为了解决如何比较向量的问题，两个向量处在两个局部坐标系中，分别用
各自的基向量表示。为了进行比较，要把以A对儿基向量表示的向量转换为通过B对儿基向量表示。

在A中，向量的表达式是VaEa, B中的向量表达式是VbEb, 
"""
r = rho * cos(phi) + rho * sin(phi)
# erho = symbols('e_rho')
"""
下面这个计算的结果是，是协变基矢量中的e_rho。
一个r,分别对rho和phi求偏导数，这又是什么意思？怎么样组合，得到两个向量？好迷惑。
"""、


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
