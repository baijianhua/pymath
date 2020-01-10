import numpy as np
from bak.animate_transform import animate_transform

A = np.column_stack([[1, 0], [2, 1]])
anim = animate_transform(A, repeat=True)
anim.save('shear.html')
anim
