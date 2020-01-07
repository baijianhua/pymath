import numpy as np

A = np.array([[2, 3],
              [4, 5]])

B = np.array([[6, 7],
              [8, 9]])

V = np.array([7, 8])


print(A @ B)
print(B @ A)
print(B.T @ A)

print("----------")
 
print(A@V)
print(V@A)
print(V@A.T)
print(V.T@A.T)
