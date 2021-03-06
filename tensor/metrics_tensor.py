import numpy as np

g1 = np.array([1.5, 0.5])
g2 = np.array([1, 2])

G = np.array([[1.5, 1],
              [0.5, 2]])
print("斜角坐标系到笛卡尔坐标系的变换矩阵(列是斜角坐标系的两个基向量笛卡尔读数)\n", G)
metricsTensor = np.array([[g1 @ g1, g1 @ g2],
                          [g2 @ g1, g2 @ g2]])

print("度量张量的第一种求法：基向量点乘\n", metricsTensor)
metricsTensor = G.T @ G
print("度量张量的第二种求法：G的转置矩阵乘以G\n", metricsTensor)
print("G的转置\n", G.T)

Va = np.array([1, 1])
print("向量V的斜角坐标读数Va\n", Va)
Ve = G @ Va
print("已知斜角读数和转换矩阵G，求迪卡尔读数Ve,需要用G@Va, 或者Va@G.T, "
      "用Va@G是不可以的\n",
      G @ Va, Va @ G.T, Va @ G)
Vb = metricsTensor @ Va
print("向量V的对偶坐标读数Vb=metricsTensor@Va\n", Vb)
print("------------------------------\n")
print("度规张量的最原始解释: 将向量的斜角坐标转换成笛卡尔坐标再运算，"
      "(Va @ G.T) @ (G @ Va)\n",
      (Va @ G.T) @ (G @ Va))

# print("度规张量的最原始解释: 将向量的斜角坐标转换成笛卡尔坐标再运算，"
#       "(Va @ G.T) @ (G @ Va)\n",
#       np.matmul( np.matmul(Va, G.T), np.matmul(G, Va)))

print("------------------------------\n")
print("笛卡尔点乘Ve@Ve\n", Ve @ Ve)

print("对偶点乘Vb@Va Va@Vb\n", Vb @ Va, Va @ Vb)
print("用度量张量求长度\n", Va @ metricsTensor @ Va)
