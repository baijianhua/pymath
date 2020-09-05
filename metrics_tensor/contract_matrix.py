from sympy import *

# commutative=False 用来防止x.g1变成g1.x
x, y, a, b, c, d, g1, g2, g11, g21 = symbols("x, y, a, b, c, d, g1, g2, g1',g2'", commutative=False)
E, F, G = symbols("E, F, G", commutative=False)
GG = Matrix([[a, c], [b, d]])
v = Matrix([UnevaluatedExpr(x), UnevaluatedExpr(y)])
v_alg = UnevaluatedExpr(x)*UnevaluatedExpr(g1)+UnevaluatedExpr(y)*UnevaluatedExpr(g2)
pprint(G)
pprint(v)
pprint(v.T)

exp = UnevaluatedExpr(v.T) * UnevaluatedExpr(G) * UnevaluatedExpr(v)
pprint(exp)
pprint(exp.doit())
print("---------------")
vv = UnevaluatedExpr(v.T*v)
P = UnevaluatedExpr(x)*UnevaluatedExpr(g1) + UnevaluatedExpr(y)*UnevaluatedExpr(g2)
PP = P*P
print_latex(PP.expand())
GG = Matrix([[E, F], [F, G]])
contract_matrix = UnevaluatedExpr(v.T)*UnevaluatedExpr(GG)*UnevaluatedExpr(v)
pprint(contract_matrix)
print_latex(contract_matrix)
# pprint(vv)
# vv_alg = v_alg * v_alg
# pprint(vv_alg.expand())
