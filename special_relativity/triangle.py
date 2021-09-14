from sympy import *


# t1 静止坐标系的时间
# t 运动坐标系的时间

def square(num):
    return num * num


theta, c, v = symbols('theta c v')
t = Symbol('t', nonnegative=true)
t1 = Symbol('t1', nonnegative=true)

va = 0
eq = Eq(square(c * t1), square(c * t * cos(theta)) + square(v * t1 + c * t * sin(theta)))
print_latex(solveset(eq, t))
print_latex(solveset(eq, t1))

print("-----------------")

print_latex(solve(eq, t)[0].subs(theta, va).simplify())
print_latex(solve(eq, t1)[0].subs(theta, va).simplify())

print("cos=", cos(va), "sin=", sin(va))

eq1 = Eq(square(c * t) + square(v * t1), square(c * t1))
print_latex(eq1)
print_latex(solveset(eq1, t))
print_latex(solveset(eq1, t1))


"""
到底想要求什么东西？是想要求运动者的一秒是静止者的多久，或者反过来
那么一秒是怎么定义的？是光通过特定距离的时间。
当选择垂直于运动方向，运动者的速度不影响不影响自己观测光行速度。——这个说法不对，即使方向相同也不影响。

"""
