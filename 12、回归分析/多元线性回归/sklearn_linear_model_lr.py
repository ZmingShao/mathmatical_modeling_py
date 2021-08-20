# 利用模块 sklearn. linear_model 中的函数 LinearRegression 求解
import numpy as np
from sklearn.linear_model import LinearRegression

a = np.loadtxt("Pdata12_1.txt")  # 加载表中x1,x2,y的13行3列数据
md = LinearRegression().fit(a[:, :2], a[:, 2])  # 构建并拟合模型
y = md.predict(a[:, :2])  # 求预测值

# 输出回归系数
b0 = md.intercept_
b12 = md.coef_

R2 = md.score(a[:, :2], a[:, 2])  # 计算R^2
print(f"b0={b0:.4f} \n b12={b12[0]:.4f}, {b12[1]:10.4f}")
print(f"拟合优度R^2={R2:.4f}")
