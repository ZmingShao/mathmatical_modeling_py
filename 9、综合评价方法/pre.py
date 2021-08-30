# 综合评价数据预处理

import numpy as np
import pandas as pd
import openpyxl

a = np.loadtxt("Pdata9_1_1.txt", )
R1 = a.copy()
R2 = a.copy()
R3 = a.copy()  # 初始化
# 注意不能写成R1=a,它们的内存地址一样，R1改变时，a也改变

# 极大型指标
for j in [0, 1, 2, 4, 5]:
    R1[:, j] = R1[:, j] / np.linalg.norm(R1[:, j])  # 向量归一化
    R2[:, j] = R2[:, j] / max(R2[:, j])  # 比例变换
    R3[:, j] = (R3[:, j] - min(R3[:, j])) / (max(R3[:, j]) - min(R3[:, j]))  # 极差变换法

# 极小型指标
for i in [3]:
    R1[:, i] = 1 - R1[:, i] / np.linalg.norm(R1[:, i])  # 向量归一化
    R2[:, i] = min(R2[:, i]) / R2[:, i]  # 比例变换
    R3[:, i] = (max(R3[:, i]) - R3[:, i]) / (max(R3[:, i]) - min(R3[:, i]))  # 极差变换法

# 把数据写入文本文件，供下面使用
np.savetxt("Pdata9_1_2.txt", R1)
np.savetxt("Pdata9_1_3.txt", R2)
np.savetxt("Pdata9_1_4.txt", R3)

# 生成DataFrame类型数据
DR1 = pd.DataFrame(R1)
DR2 = pd.DataFrame(R2)
DR3 = pd.DataFrame(R3)

# 把DRi写入Excel文件i号表单中,方便做表
f = pd.ExcelWriter('Pdata9_1_5.xlsx')  # 创建文件对象
DR1.to_excel(f, "sheet1")
DR2.to_excel(f, "sheet2")
DR3.to_excel(f, "Sheet3")
f.save()
print('successfully saved')
