# 用scipy.optimize模块求解

from scipy.optimize import linprog
import numpy as np

c = np.array([-3, 1])
A = [[3, -2], [-5, -4], [2, 1], [4, -1]]
b = [[3], [-10], [5], [6]]
Aeq = []
beq = []
LB = [0, 0]
UB = [None] * len(c)  # 生成3个None的列表
bound = tuple(zip(LB, UB))  # 生成决策向量界限的元组
res = linprog(c, A, b, None, None, bound)
print("目标函数的最小值：", res.fun)
print("最优解为：", res.x)
