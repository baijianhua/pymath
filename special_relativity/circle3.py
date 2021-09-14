from sympy import *

c, t, v, x1, t1 = symbols("c t v x' t'")
a = Symbol("alpha")
eq1 = Eq((c * t1) ** 2, (c * t) ** 2 + (v * t) ** 2 - 2 * c * t * v * t * (v * t + x1) / (c * t))
pprint(eq1)

tt = solve(eq1, t)[1]
#
# tt = tt.cancel()
pprint(tt)

# 如果按矢量相加法则
# ct = vt + ct1, 其中ct1可以表示为

ttt = solve(eq1, t1)
pprint(ttt)
