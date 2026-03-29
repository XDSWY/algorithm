"""
题目描述
首先所有的灯都是关的（注意是关！），编号为 1 的人走过来，把是 1 的倍数的灯全部打开，编号为 2 的人把是 2 的倍数的灯全部关上，
编号为 3 的人又把是 3 的倍数的灯开的关上，关的开起来……直到第 N 个人为止。
给定 N，求 N 轮之后，还有哪几盏是开着的。
输入格式
一个数 N，表示灯的个数和操作的轮数。
输出格式
若干数，表示开着的电灯编号。

输入
5
输出
1 4
"""
N = int(input())
lst = []

for i in range(1, N+1):
    lst.append(i)

for i in range(2, N + 1):
    for j in range(1, N + 1):
        if i * j <= N:
            if i*j in lst:
                lst.remove(i*j)
            elif i*j not in lst:
                lst.append(i*j)

result = ' '.join(map(str, lst))
print(result)


# 只有完全平方数的灯最后是开着的。
# N = int(input())
# result = [str(i * i) for i in range(1, int(N ** 0.5) + 1)]
# print(' '.join(result))