# 常用综合评价模型

import numpy as np
from scipy.stats import rankdata

a = np.loadtxt("Pdata9_1_3.txt")

# TOPSIS
c_plus = a.max(axis=0)  # 逐列求最大值
c_minus = a.min(axis=0)  # 逐列求最小值
print("正理想解=", c_plus, "负理想解=", c_minus)
d1 = np.linalg.norm(a - c_plus, axis=1)  # 求到正理想解的距离
d2 = np.linalg.norm(a - c_minus, axis=1)  # 求到负理想解的距离
print(d1, d2)  # 显示到正理想解和负理想解的距离
f1 = d2 / (d1 + d2)
print("TOPSIS的评价值为：", f1)

# 灰色关联分析
t = c_plus - a  # 计算参考序列与每个序列的差
m_min = t.min()
m_max = t.max()  # 计算最小差和最大差
rho = 0.5  # 分辨系数
xs = (m_min + rho * m_max) / (t + rho * m_max)  # 计算灰色关联系数
f2 = xs.mean(axis=1)  # 求每一行的均值
print("\n关联系数=", xs, '\n关联度=', f2)  # 显示灰色关联系数和灰色关联度

# 熵权法
"""
注意熵权法要求预处理后的数据，各个元素均大于零
"""
[n, m] = a.shape
cs = a.sum(axis=0)  # 逐列求和
P = 1 / cs * a  # 求特征比重矩阵
e = -(P * np.log(P)).sum(axis=0) / np.log(n)  # 计算熵值
g = 1 - e  # 计算差异系数
w = g / sum(g)  # 计算权重
F = P @ w  # 计算各对象的评价值
print("\nP={}\n,e={}\n,g={}\n,w={}\nF={}".format(P, e, g, w, F))

# RSR秩和比
R = [rankdata(a[:, i]) for i in np.arange(6)]  # 求每一列的秩
R = np.array(R).T  # 构造秩矩阵
print("\n秩矩阵为：\n", R)
RSR = R.mean(axis=1) / n
print("RSR=", RSR)
