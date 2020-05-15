from sympy import *
from sympy.core.function import UndefinedFunction
from sympy.printing.latex import LatexPrinter


class MyLatexPrinter(LatexPrinter):
    def _print_Derivative(self, expr):
        # Only print the shortened way for functions of symbols
        function, *vars = expr.args
        print("test........")
        if not isinstance(type(function), UndefinedFunction) or not all(isinstance(i, Symbol) for i in vars):
            return super()._print_Derivative(expr)
        return r'%s_{%s}' % (self._print(Symbol(function.func.__name__)), ' '.join([self._print(i) for i in vars]))


init_printing(latex_printer=MyLatexPrinter().doprint)
x, delta_x, t = symbols("x, delta_x, t")
fx = Function('f')(x)
print_latex(diff(fx, x, evaluated=false))

f = Function("f")(x, t)


print_latex(f.diff(x, x))


