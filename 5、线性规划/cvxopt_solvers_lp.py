#
import numpy
from cvxopt import matrix, solvers


c = matrix([-1., 2, 3])
A = matrix([[-2., 1, 1], [3, -1, -2], [-1, 0, 0], [0, -1, 0]]).T
b = matrix([9., -4, 10, 0])
Aeq = matrix([4., -2, -1]).T
beq = matrix(-6.)
sol = solvers.lp(c, A, b, Aeq, beq)
print("最优解为：\n", sol['x'])
print("最优值为：", sol['primal objective'])
