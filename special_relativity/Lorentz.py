from sympy import *

# sympy化简 https://blog.csdn.net/FYZDMMCpp/article/details/86611948

# 静止坐标系
x, y, z, t, c = symbols("x,y,z,t,c")
# 运动坐标系
x1, y1, z1, t1 = symbols("x',y',z',t'")
gamma, v = symbols('gamma, v')
eq1 = Eq(x, gamma * (x1 + v * t1))
eq2 = Eq(x1, gamma * (x - v * t))

# t1 的表达式，用x,v,x1表示
# x1 的表达式，用x,v,t表示
t1_exp = solve(eq1, t1)[0]
x1_exp = solve(eq2, x1)[0]

# x 的表达式，用x1,v,t1表示
x_exp = solve(eq1, x)[0]
# x*x', 并代入x = ct, x'=ct'
x_x1_exp = (x_exp * x1_exp).subs({x: c * t, x1: c * t1})
# 列方程
eq3 = Eq(c * t * c * t1, x_x1_exp)
gamma_exps = solve(eq3, gamma)
# 求 gamma的值，因为gamma开平方，所以取[1]，正值，忽略负值
gamma_exp = gamma_exps[1]
# print_latex(gamma_exps)
pprint.pformat(gamma, "=", gamma_exp)
pprint(cancel(gamma_exp))


# 将gamma带回t1的表达式
t1_final = solve(Eq(t1_exp.subs({gamma: gamma_exp, x: c*t, x1: c*t1}), t1), t1)
pprint(t1_final)

