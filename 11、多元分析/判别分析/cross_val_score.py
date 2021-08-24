# 交叉检验

import numpy as np
import pandas as pd
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis as LDA
from sklearn.model_selection import cross_val_score

a = pd.read_excel("Pdata11_2.xlsx", header=None)
b = a.values
x0 = b[:-2, 1:-1].astype(float)  # 提取已知样本点的观测值
y0 = b[:-2, -1].astype(int)
model = LDA()
print(cross_val_score(model, x0, y0, cv=2))
