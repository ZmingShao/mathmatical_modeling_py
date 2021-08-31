# 岭回归
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import Ridge, RidgeCV
from scipy.stats import zscore

a = np.loadtxt("Pdata12_3.txt")
n = a.shape[1] - 1  # 自变量的总个数
aa = zscore(a)  # 数据标准化

# 提出自变量和因变量观测值矩阵
x = aa[:, :n]
y = aa[:, n]

# 画岭迹图
b = []  # 用于存储回归系数的空列表
kk = np.logspace(-4, 0, 100)  # 循环迭代的不同k值
for k in kk:
    md = Ridge(alpha=k).fit(x, y)
    b.append(md.coef_)
st = ['s-r', '*-k', 'p-b']  # 下面画图的控制字符串
for i in range(3):
    plt.plot(kk, np.array(b)[:, i], st[i])
plt.legend(['$x_1$', '$x_2$', '$x_3$'], fontsize=15)
plt.show()

# 使用函数 RidgeCV 确定最佳k值
mdcv = RidgeCV(alphas=np.logspace(-4, 0, 100)).fit(x, y)
print("最优k=", mdcv.alpha_)
# md0=Ridge(mdcv.alpha_).fit(x,y)  #构建并拟合模型

# 由岭迹图主观确定k值（推荐）
# 观察岭迹曲线，原则上应该选取使βˆ k()稳定的最小k值，本例为0.4
md0 = Ridge(0.4).fit(x, y)  # 构建并拟合模型

# 提出标准化数据的回归系数b1,b2,b3
cs0 = md0.coef_
print("标准化数据的所有回归系数为：", cs0)

# mu = np.mean(a, axis=0)
# s = np.std(a, axis=0, ddof=1)  # 计算所有指标的均值和标准差
# params = [mu[-1] - s[-1] * sum(cs0 * mu[:-1] / s[:-1]), s[-1] * cs0 / s[:-1]]
# print("原数据的回归系数为：", params)

# 拟合优度
print("拟合优度：", md0.score(x, y))
