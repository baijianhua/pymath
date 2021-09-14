"""
测试矩阵乘法
"""
from numpy import mat, array, multiply

a = mat([1, 2])
print(a*3)

m1 = mat([[1, 2],
          [3, 4]])

m2 = mat([[5, 6],
          [7, 8]])

print(m1*m2)
print(m1@m2)
print(multiply(m1, m2))


