"""
问题描述
小蓝从左到右种了 n棵小树，第 i 棵树的高度为 h i，相邻树的间隔相同。
小蓝想挪走一些树，使得剩下的树等间隔分布，且从左到右高度逐渐上升（相邻两棵树高度满足右边的比左边的高），小蓝想知道最多能留下多少棵树。

输入格式
输入的第一行包含一个正整数 n。
第二行包含 n 个正整数 h1,h2,…,hn，相邻整数之间使用一个空格分隔。

输出格式
输出一行包含一个整数，表示最多能留下的树的数量。

样例输入
6
3 5 4 7 6 7

样例输出
3
样例说明留下第 1、3、5 棵树，它们等间隔且从左到右高度逐渐上升。
"""
import os
import sys

# n = int(input())
# integer = list(map(int, input().split()))
# result = 0
#
# a, b = 0, 0
# while b < n:
#   b += 1
#   if integer[b] > integer[a]:
#     a = b
#     b = a + 1
#     result += 1
#   else:
#     b += 1
#
# print(result + 1)

n = int(input())
h = list(map(int, input().split()))

result = 1  # 至少可以留 1 棵树

# 枚举公差 d
for d in range(1, n):
    # dp[i] 表示以 i 结尾的、公差为 d 的最长序列长度
    dp = [1] * n

    for i in range(n):
        # 找前一个位置 j = i - d
        j = i - d
        if j >= 0 and h[i] > h[j]:
            dp[i] = dp[j] + 1
            result = max(result, dp[i])

print(result)

