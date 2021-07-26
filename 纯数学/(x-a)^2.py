from sympy import symbols, diff, pprint

z, x, a = symbols("z x a")
w, b = symbols("w b")
y = (x-a)**2
pprint(diff(y, x))

z = w*x+b
pprint(diff(z, w))

