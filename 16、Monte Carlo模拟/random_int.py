#使用随机数模拟概率
from numpy.random import rand
import numpy as np
n=100000
a=rand(n)   # 均匀分布
n1=np.sum(a<=0.2)
n2=np.sum((a>0.2) & (a<=0.5))
n3=np.sum(a>0.5)
f=np.array([n1,n2,n3])/n
print(f)
