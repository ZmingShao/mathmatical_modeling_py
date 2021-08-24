# 层次聚类——最短距离

import numpy as np
from sklearn import preprocessing as pp
import scipy.cluster.hierarchy as sch
import matplotlib.pyplot as plt

a = np.loadtxt("Pdata11_11.txt")
b = pp.minmax_scale(a.T)  # 数据规格化
d = sch.distance.pdist(b)  # 求对象之间的两两距离向量
# dd = sch.distance.squareform(d)  # 转换为矩阵格式
z = sch.linkage(d)
print(z)  # 进行聚类并显示
s = [str(i) for i in range(b.shape[0])]
plt.rc('font', size=16)
sch.dendrogram(z, labels=np.array(s))
plt.show()  # 画聚类图
