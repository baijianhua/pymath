"""
偏微分一定要显示一个表达式，而不是直接一个函数名，这个看起来和数学里面用的不一样

或许应该直接写出来这个函数名形式的偏微分，而真正的表达式才让sympy来输出。
"""
from sympy import *
from common import plot_latex

x, y, z = symbols('x_{1}^2 y z1')
expr1 = exp(x*y*z)
# r2 = latex(diff(expr1, x, evaluate=False))
r3 = latex(diff((x, y), x, evaluate=False))
# plot_latex(r3)

fxy = Function('x')
plot_latex(latex(fxy) )