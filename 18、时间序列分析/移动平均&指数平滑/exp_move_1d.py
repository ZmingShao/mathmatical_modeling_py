# 一次指数平滑
"""
1. a的选取：
    如果时间序列波动不大，比较平稳，则α 应取小一点，如 0.1～0.5，以减少修正幅度，使预测模型能包含较长时间序列的信息；
    如果时间序列具有迅速且明显的变动倾向，则α 应取大一点，如 0.6～0.8，使预测模型灵敏度高一些，以便迅速跟上数据的变化。
2. 初始值的选取：
    当时间序列的数据较多，比如在 20 个以上时，初始值对以后的预测值影响很少，可选用第一期数据为初始值；
    如果时间序列的数据较少，在 20 个以下时，初始值对以后的预测值影响很大，这时，就必须认真研究如何正确确定初始值。一般以最初几期实际值的平均值作为初始值。
"""

import numpy as np
import pandas as pd
from statsmodels.tsa.api import SimpleExpSmoothing
from sklearn.metrics import mean_squared_error
from math import sqrt

y = np.array([4.81, 4.8, 4.73, 4.7, 4.7, 4.73, 4.75, 4.75, 5.43, 5.78, 5.85])
y_train = y[:-1]
y_test = y[-1:]


# def ExpMove(y, a):
#     n = len(y)
#     M = np.zeros(n)
#     M[0] = (y[0] + y[1]) / 2
#     for i in range(1, len(y)):
#         M[i] = a * y[i - 1] + (1 - a) * M[i - 1]
#     return M
#
#
# yt1 = ExpMove(y, 0.2)
# yt2 = ExpMove(y, 0.5)
# yt3 = ExpMove(y, 0.8)
# s1 = np.sqrt(((y - yt1) ** 2).mean())
# s2 = np.sqrt(((y - yt2) ** 2).mean())
# s3 = np.sqrt(((y - yt3) ** 2).mean())
# d = pd.DataFrame(np.c_[yt1, yt2, yt3])
# f = pd.ExcelWriter("Pdata18_2.xlsx")
# d.to_excel(f)
# f.close()  # 数据写入Excel文件，便于做表
# print("预测的标准误差分别为：", s1, s2, s3)  # 输出预测的标准误差
# yh = 0.8 * y_train[-1] + 0.2 * yt3[-1]
# print("下一期的预测值为：", yh)

fit1 = SimpleExpSmoothing(y_train).fit(smoothing_level=0.2, optimized=False)
yh1 = fit1.forecast(len(y_test))
s1 = sqrt(mean_squared_error(y_test, yh1))
fit2 = SimpleExpSmoothing(y_train).fit(smoothing_level=0.5, optimized=False)
yh2 = fit2.forecast(len(y_test))
s2 = sqrt(mean_squared_error(y_test, yh2))
fit3 = SimpleExpSmoothing(y_train).fit(smoothing_level=0.8, optimized=False)
yh3 = fit3.forecast(len(y_test))
s3 = sqrt(mean_squared_error(y_test, yh3))
print("预测的标准误差分别为：", s1, s2, s3)  # 输出预测的标准误差
print("下一期的预测值为：", yh1, yh2, yh3)
