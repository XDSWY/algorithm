"""
题目描述
输入一组勾股数 a,b,c(互相不等)
输入格式
一行，包含三个正整数，即勾股数 a,b,c（无大小顺序）。

输出格式
一行，包含一个分数，即较小锐角的正弦值。

输入
3 5 4

输出
3/5
"""

from math import gcd

a, b, c = map(int, input().split())
lst = [a, b, c]

lst.sort()

nums = gcd(lst[0], lst[-1])

first = lst[0] / nums
last = lst[-1] / nums

print(f"{int(first)}/{int(last)}")