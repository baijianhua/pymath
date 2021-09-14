from sympy import *

# sympy化简：   https://blog.csdn.net/FYZDMMCpp/article/details/86611948
# Lorentz变换： https://baike.baidu.com/item/%E6%B4%9B%E4%BC%A6%E5%85%B9%E5%8F%98%E6%8D%A2/620820?fr=aladdin
# 静止坐标系
x, y, z, t, c = symbols("x,y,z,t,c")
# 运动坐标系
x1, y1, z1, t1 = symbols("x',y',z',t'")
gamma, v = symbols('gamma, v')
eq1 = Eq(x, gamma * (x1 + v * t1))
eq2 = Eq(x1, gamma * (x - v * t))

"""求gamma的值"""
# x1 的表达式，用x,v,t表示
x1_exp = solve(eq2, x1)[0]
# x 的表达式，用x1,v,t1表示
x_exp = solve(eq1, x)[0]
# x*x', 并代入x = ct, x'=ct'
x_times_x1 = (x_exp * x1_exp).subs({x: c * t, x1: c * t1})
# 用ct,ct' 列方程, 这时候未知数只剩下 gamma
eq3 = Eq(c * t * c * t1, x_times_x1)
gamma_exps = solve(eq3, gamma)
# 求 gamma的值，因为gamma开平方，所以取[1]，正值，忽略负值
gamma_exp = cancel(gamma_exps[1])
pprint(Eq(gamma, gamma_exp))

"""根据gamma的值，求x, x'的转换关系"""
x1_from_x = x1_exp.subs(gamma, gamma_exp)
pprint(Eq(x1, x1_from_x))
x_from_x1 = x_exp.subs(gamma, gamma_exp)
pprint(Eq(x, x_from_x1))

"""求t1，t的转换关系"""
t1_exp = factor(x_exp.subs(x1, x1_exp))
t1_exp = solve(Eq(x, t1_exp), t1)[0]
t1_exp = factor(t1_exp)
pprint(t1_exp)
t1_exp = t1_exp.subs(gamma, gamma_exp).simplify()
pprint(Eq(t1, t1_exp))

t_exp = x1_exp.subs(x, x_exp)
t_exp = solve(Eq(x1, t_exp), t)[0]
t_exp = t_exp.subs(gamma, gamma_exp).simplify()
# t_exp = factor(t_exp)
pprint(Eq(t, t_exp))
