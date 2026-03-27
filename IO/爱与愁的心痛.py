"""
题目描述
最近有 n 个不爽的事，每句话都有一个正整数刺痛值（心理承受力极差）。
爱与愁大神想知道连续 m 个刺痛值的和的最小值是多少，但是由于业务繁忙，爱与愁大神只好请你编个程序告诉他。

输入格式
第一行有两个用空格隔开的整数，分别代表 n 和 m。
第 2 到第 (n+1) 行，每行一个整数，第 (i+1) 行的整数 ai代表第 i 件事的刺痛值 ai

输出格式
输出一行一个整数，表示连续 m 个刺痛值的和的最小值是多少。

输入
8 3
1
4
7
3
1
2
4
3

输出
6
"""

n, m = list(map(int, input().split()))

result = 0

lst = []
lst2 = []

for i in range(n):
    ai = int(input())
    lst.append(ai)

for i in range(n - m + 1):
    sum = 0
    for j in range(m):
        sum += lst[i + j]
    lst2.append(sum)


result = sorted(lst2)

print(result[0])

