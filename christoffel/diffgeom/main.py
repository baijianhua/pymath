from sympy.diffgeom import Manifold, Patch
m = Manifold('M', 3)
p = Patch('P', m)
p in m.patches