# 多项式拟合

import numpy as np
import matplotlib.pyplot as plt

x0 = np.arange(0, 1.1, 0.1)
y0 = np.array([-0.447, 1.978, 3.28, 6.16, 7.08, 7.34, 7.66, 9.56, 9.48, 9.30, 11.2])
p = np.polyfit(x0, y0, 2)  # 拟合二次多项式
print("拟合二次多项式的从高次幂到低次幂系数分别为:", p)
yhat = np.polyval(p, [0.25, 0.35])
print("预测值分别为：", yhat)
plt.rc('font', size=16)
plt.plot(x0, y0, '*', x0, np.polyval(p, x0), '-')
plt.show()
