# 季节系数法——具有季节性时间序列的预测
import numpy as np

a = np.loadtxt('Pdata18_4.txt')
m, n = a.shape
amean = a.mean()  # 计算所有数据的平均值
cmean = a.mean(axis=0)  # 逐列求均值，即同季度数据的算术平均值
r = cmean / amean  # 计算季节系数
w = np.arange(1, m + 1) # w为各年的权数，按自然数列取值
yh = w.dot(a.sum(axis=1)) / w.sum()  # 计算下一年的预测值
yj = yh / n  # 计算预测年份的季度平均值
yjh = yj * r  # 计算季度预测值
print("下一年度各季度的预测值为：", yjh)
