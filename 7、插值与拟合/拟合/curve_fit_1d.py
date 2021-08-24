# 任意函数拟合(一元)

import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt

x0 = np.arange(0, 1.1, 0.1)
y0 = np.array([-0.447, 1.978, 3.28, 6.16, 7.08, 7.34, 7.66, 9.56, 9.48, 9.30, 11.2])
y = lambda x, a, b, c :a * x ** 2 + b * x + c
popt, pcov = curve_fit(y, x0, y0)
print("a，b，c的拟合值为：", popt)
plt.rc('font', size=16)
plt.plot(x0, y0, '*', x0, y(x0, *popt), '-')
plt.show()