"""

判断是否为水仙花数

"""

num = int(input("请输入"))

while (num < 100 or num > 999):
    print("输入数非三位数,请重新输入:", end = ' ')
    num = int(input())

a = num // 100
b = (num - a * 100) // 10
c = num % 10


if num == a**3+b**3+c**3 :
    print("%d是水仙花数"%num)
else:
    print("%d不是水仙花数"%num)