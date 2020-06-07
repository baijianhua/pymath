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
x_x1_exp = (x_exp * x1_exp).subs({x: c * t, x1: c * t1})
# 用ct,ct' 列方程, 这时候未知数只剩下 gamma
eq3 = Eq(c * t * c * t1, x_x1_exp)
gamma_exps = solve(eq3, gamma)
# 求 gamma的值，因为gamma开平方，所以取[1]，正值，忽略负值
gamma_exp = gamma_exps[1]
# print_latex(gamma_exps)
# pprint(Eq(gamma, gamma_exp))
pprint(Eq(gamma, cancel(gamma_exp)))

"""求t1，t的转换关系"""
# 将gamma带回t1的表达式
# t1 的表达式，用x,v,x1表示
t1_exp = solve(eq1, t1)[0]
eq4 = t1_exp.subs({gamma: gamma_exp, x1: c*t1})
t1_1 = solve(Eq(t1, eq4), t1)[0]
# pprint(Eq(t1, t1_1))

t1_final = solve(Eq(t1_exp.subs({gamma: gamma_exp, x: c * t, x1: c * t1}), t1), t1)[0]
# pprint(Eq(t1, t1_final))
t_final = solve(Eq(t1, t1_final), t)[0]
# pprint(Eq(t, t_final))

"""根据gamma的值，求x, x'的转换关系"""
x_x1_eq = Eq(x1, x1_exp).subs(gamma, gamma_exp)
x1_from_x = solve(x_x1_eq, x1)[0]
pprint(Eq(x1, x1_from_x))
x_from_x1 = solve(x_x1_eq, x)[0]
# 还要将t换成t'才行。不能含有S坐标系的东西。t是S坐标系的。
pprint(Eq(x, x_from_x1))


