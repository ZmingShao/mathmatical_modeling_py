# KMeans聚类
"""
如果原始数据集存在量纲上的差异，就必须对其进行标准化的预处理
数据集的标准化处理可以借助于 sklearn 子模块 preprocessing 中的 scale 函数或minmax_scale 函数
"""

import numpy as np
from sklearn.cluster import KMeans

a = np.array([[1, 3], [1.5, 3.2], [1.3, 2.8], [3, 1]])
md = KMeans(n_clusters=2)  # 构建模型
md.fit(a)  # 求解模型
labels = md.labels_  # 提取聚类标签
centers = md.cluster_centers_  # 提取聚类中心,每一行是一个聚类中心
print(labels, '\n-----------\n', centers)
