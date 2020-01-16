"""
抽签算法
"""
left = 14
possibility = 1 / pow(2, left)
total_machine = pow(10, 6)
print("possibility=", possibility, "total machine=", total_machine, "selected=", possibility * total_machine)
