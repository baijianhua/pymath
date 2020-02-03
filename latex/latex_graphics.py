from sympy import *
import warnings
from common import plot_latex

# 去除cp_math里面的警告
with warnings.catch_warnings():
    warnings.filterwarnings("ignore", category=SyntaxWarning)

a, b, c, d = symbols('a b c d')
M = Matrix([[a, b],
            [c, d]])

print(M)
print(M.T)
lat = latex(M.T @ M)
print(lat)

plot_latex(lat)
