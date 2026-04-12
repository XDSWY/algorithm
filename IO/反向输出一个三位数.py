"""
题目描述
将一个三位数反向输出，例如输入 358，反向输出 853。

输入格式
一个三位数 n。

输出格式
反向输出 n。

输入
100

输出
001

输入
001

输出
100

"""

n = input()
s = list(n)

new = s[::-1]
result = ''.join(map(str, new))

print(result)

# n = input().strip()
# print(n[::-1])
