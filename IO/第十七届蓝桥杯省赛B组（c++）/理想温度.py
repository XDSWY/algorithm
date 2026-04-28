"""
题目描述
一条工业流水线上排列着 n 个温度传感器。当前各个传感器测得的温度记录在数组 A 中，而各传感器对应的理想标准温度记录在数组 B 中
（即 Ai为第 i 个传感器的当前温度，B i为第 i 个传感器的理想温度）。
为了让尽可能多的传感器达到理想温度，你可以进行一次区域温度补偿操作：

在流水线上划定一段连续的传感器区间 [l,r]（即第 l 个到第 r 个传感器）。
输入一个温度补偿值 k（k 为任意整数），使得该区间内所有传感器的当前温度都加上 k。
请问在执行完这一次校准操作后，最多能使多少个传感器的温度恰好等于其对应的理想标准温度？

输入格式
第一行包含一个整数 n，表示传感器的数量。
第二行包含n个整数 A1,A2,…,An，表示各传感器的当前温度。
第三行包含 n 个整数 B1,B2,…,Bn，表示各传感器对应的理想标准温度。

输出格式
输出一行，包含一个整数，表示补偿操作后处于理想温度的传感器最大数量。

输入
5
1 2 3 4 5
2 3 2 3 2

输出
2
"""

n = int(input())
An = list(map(int, input().split()))
Bn = list(map(int, input().split()))
lst = [0] * n

for i in range(n):
    lst[i] = Bn[i] - An[i]

new_lst = []
tot = 0
count = 0

max_len = 1
cur_len = 1
for i in range(1, n):
    if lst[i] == lst[i-1]:
        cur_len += 1
        max_len = max(max_len, cur_len)
    else:
        cur_len = 1


max_zero = 0
cur_zero = 0
for v in lst:
    if v == 0:
        cur_zero += 1
        max_zero = max(max_zero, cur_zero)
    else:
        cur_zero = 0

print(max(max_len, max_zero))



