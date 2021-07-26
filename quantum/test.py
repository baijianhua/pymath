from sympy import *

# x = Symbol("x")
# exp = 2*Integral(atan(x)/(1+x**2))
# pprint(exp)
# print(exp.doit())
exp = 1-2*sin(1)*cos(1)*0.1

print("result=", exp.evalf())
