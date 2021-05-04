#
import cvxpy as cp
import numpy as np
import pandas as pd

c = np.array([1, -1, 1])
#A = np.array([[-2, 1, 1], [3, -1, -2]])
#b = np.array([[9], [-4]])
Aeq = np.array([[1, 2, 3], [4, 5, -6]])
beq = np.array([6, 6]).T
x = cp.Variable(3)
obj = cp.Minimize(c @ x) # 构造目标函数
con = [Aeq @ x == beq, x >= 0]  # 构造约束条件
prob = cp.Problem(obj, con)  # 构造模型
prob.solve(solver='GLPK_MI', verbose=True)  # 求解模型
print("最优值为：", prob.value)
print("最优解为：\n", x.value)
