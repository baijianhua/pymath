from mpmath import *


def f1(z):
    return z


def f2(z):
    return z ** 3


def f3(z):
    return (z ** 4 - 1) ** (1 / 4)


def f4(z):
    return 1 / z


def f5(z):
    return atan(z)


def f6(z):
    return sqrt(z)


cplot(f1)
# cplot(f2)
# cplot(f3)
# cplot(f4)
# cplot(f5)
# cplot(f6)
