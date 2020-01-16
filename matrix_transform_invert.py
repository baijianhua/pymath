from numpy import mat

left = 14
possibility = 1 / pow(2, left)
total_machine = pow(10, 6)
print("possibility=", possibility, "total machine=", total_machine, "selected=", possibility * total_machine)

m = mat([[2, 3, 1],
         [4, 5, 6],
         [7, 8, 9],
         ])

print(m.T.I)
print(m.I.T)
