# 简单一次移动平均
"""
当预测目标的基本趋势是在某一水平上下波动时，可用一次移动平均方法建立预测模型
当预测目标的基本趋势与某一线性模型相吻合时，常用二次移动平均法。当序列同时存在线性趋势与周期波动时，可用趋势移动平均法建立预测模型
"""
import numpy as np

y = np.array([423, 358, 434, 445, 527, 429, 426, 502, 480, 384, 427, 446])


def MoveAverage(y, N):
    Mt = ['*'] * N
    for i in range(N + 1, len(y) + 2):
        M = y[i - (N + 1):i - 1].mean()
        Mt.append(M)
    return Mt


yt3 = MoveAverage(y, 3)
s3 = np.sqrt(((y[3:] - yt3[3:-1]) ** 2).mean())
yt5 = MoveAverage(y, 5)
s5 = np.sqrt(((y[5:] - yt5[5:-1]) ** 2).mean())
print('N=3时,预测值：', yt3, '，预测的标准误差：', s3)
print('N=5时,预测值：', yt5, '，预测的标准误差：', s5)
