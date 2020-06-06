from sympy import *

a, b, theta, c, t, t1, v = symbols('a b theta c t t1 v')
eq = Eq(pow(c*t1*cos(theta), 2) + pow(v*t, 2), pow(c*t, 2))
print_latex(solve(eq, t)[0].subs(theta, pi/6).simplify())
print_latex(solve(eq, t1)[0].subs(theta, pi/6).simplify())
"""
到底想要求什么东西？是想要求运动者的一秒是静止者的多久，或者反过来
那么一秒是怎么定义的？是光通过特定距离的时间。
当选择垂直于运动方向，运动者的速度不影响不影响自己观测光行速度。——这个说法不对，即使方向相同也不影响。

"""
