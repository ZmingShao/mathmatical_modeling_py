"""

计算并打印地球上A,B两点的大圆弧距离d

"""

from numpy import arccos, cos, sin

x1, y1 = eval(input("请输入A点的经度和纬度"))
x2, y2 = eval(input("请输入B点的经度和纬度"))

R = 6370

d = R * arccos(cos(x1 - x2) * cos(y1) * cos(y2) + sin(y1) * sin(y2))
print(x1, y1, x2, y2, d)
