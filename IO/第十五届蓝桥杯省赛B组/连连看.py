"""
问题描述
小蓝正在和朋友们玩一种新的连连看游戏。在一个 n×m 的矩形网格中，每个格子中都有一个整数，第
i 行第 j 列上的整数为 A i,j 。玩家需要在这个网格中寻找一对格子
(a,b)−(c,d) 使得这两个格子中的整数 A(a,b)和 A(c,d)相等，且它们的位置满足
∣a−c∣=∣b−d∣>0 。请问在这个 n×m 的矩形网格中有多少对这样的格子满足条件。

输入格式
输入的第一行包含两个正整数 n,m，用一个空格分隔。

接下来 n 行，第 i 行包含 m 个正整数

A(i,1),A(i,2),⋯,A(i,m)，相邻整数之间使用一个空格分隔。

输出格式
输出一行包含一个整数表示答案。

样例输入
3 2
1 2
2 3
3 2

样例输出
6

样例说明
一共有以下 6 对格子：
(1,2)−(2,1)，(2,2)−(3,1)，(2,1)−(3,2)，
(2,1)−(1,2)，(3,1)−(2,2)，(3,2)−(2,1)。
"""

import os
import sys

n, m = map(int, input().split())
result = 0
lst = []

for i in range(n):
  row =  list(map(int,input().split()))
  lst.append(row)

for i in range(n):
    for j in range(m):
        k = 1
        while (i + k) < n  and (j + k) < m:
            if lst[i][j] == lst[i + k][j + k]:
                result += 2
            k += 1

        k = 1
        while (i + k) < n and (j - k) >= 0:
            if  lst[i][j] == lst[i + k][j - k]:
                result += 2
            k += 1

print(result)


