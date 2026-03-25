"""
题目描述
设有一个 N×M 方格的棋盘 (1≤N≤100,1≤M≤100)求出该棋盘中包含有多少个正方形、多少个长方形（不包括正方形）。

输入格式
一行两个整数 N,M。
输出格式
一行两个整数，表示正方形的个数与长方形的个数。

输入
2 3

输出
8 10
"""

N, M = map(int,input().split())

sum_N = 0
sum_M = 0

if N > M:
    for i in range(M):
        sum_N += (N-i)*(M-i)
else:
    for i in range(N):
        sum_N += (N-i)*(M-i)

sums_M = 0
sums_N = 0

for i in range(M):
    sums_M += M-i

for i in range(N):
    sums_N += N-i

sum_M = (sums_M * sums_N) - sum_N


print(sum_N,sum_M)
