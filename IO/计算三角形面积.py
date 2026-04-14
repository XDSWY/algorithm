"""
题目描述
平面上有一个三角形，它的三个顶点坐标分别为 (x 1,y 1),(x 2,y 2),(x 3,y 3)，那么请问这个三角形的面积是多少。

输入格式
输入仅一行，包括 6 个双精度浮点数，分别对应 x 1,y 1,x 2,y 2,x 3,y 3。坐标的绝对值不超过 100，且小数点后最多只有一位。

输出格式
输出也是一行，输出三角形的面积，精确到小数点后两位。

输入
0 0 4 0 0 3

输出
6.00
"""

from math import sqrt

x1, y1, x2, y2, x3, y3 = map(float,input().split())

len_12 = sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
len_13 = sqrt((x3 - x1) ** 2 + (y3 - y1) ** 2)
len_23 = sqrt((x3 - x2) ** 2 + (y3 - y2) ** 2)

s = (len_12 + len_13 + len_23) / 2

result = sqrt(s * (s - len_12) * (s - len_13) * (s - len_23))

print(f"{result:.2f}")