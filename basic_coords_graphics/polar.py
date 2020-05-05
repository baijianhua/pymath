"""
Demo of a line plot on a polar axis.
"""
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.axes import Axes

from sympy import *
from sympy.diffgeom import *

erhohat = symbols('ehat')
rho, phi = symbols('rho, phi')
x, y = symbols('x, y')
fx = rho * cos(phi)
fy = rho * sin(phi)

dyphi = diff(fy, phi)
dxphi = diff(fx, phi)

dxrho = diff(fx, rho)
dyrho = diff(fy, rho)

print("erhohat", "=", dxrho, dyrho)
pprint(dxrho)
pprint(dyrho)

pprint(dxphi)
pprint(dyphi)


pprint(diff(dxphi, phi, evaluate=False))
pprint(diff(dyphi, phi))
