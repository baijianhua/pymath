from numpy import mat

'''
测试A的转置的逆与A的逆的转置是否相等
'''
m = mat([[2, 3, 1],
         [4, 5, 6],
         [7, 8, 9],
         ])

print(m.T.I)
print(m.I.T)
