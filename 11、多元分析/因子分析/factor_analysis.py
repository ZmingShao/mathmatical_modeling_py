# 因子分析

import numpy as np

r = np.array([[1, 1 / 5, -1 / 5], [1 / 5, 1, -2 / 5], [-1 / 5, -2 / 5, 1]])
[val, vec] = np.linalg.eig(r)  # 求相关系数阵的特征值和特征向量
vec *= np.sign(vec.sum(axis=0))
# A1 = np.tile(np.sqrt(val), (3, 1)) * vec
A = vec * np.sqrt(val)  # 利用广播运算求载荷矩阵
print('val:', val, '\n----------\n', 'A:', A)
num = int(input("请输入选择公共因子的个数："))
A = A[:, :num]  # 提出num个因子的载荷矩阵
Ac = np.sum(A ** 2, axis=0)  # 逐列元素求和
Ar = np.sum(A ** 2, axis=1)  # 逐行元素求和
print("对x的贡献为：", Ac)
print("共同度为：", Ar)
