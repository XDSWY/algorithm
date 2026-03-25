"""
题目描述
现代数学的著名证明之一是 Georg Cantor 证明了有理数是可枚举的。他是用下面这一张表来证明这一命题的：

1/1 1/2 1/3 1/4 1/5 ...
2/1 2/2 2/3 2/4 ...
3/1 3/2 3/3 ...
4/1 4/2 ...
5/1 ...

这次与 NOIp1999 第一题不同的是：这次需输入两个分数（不一定是最简分数），算出这两个分数的积（注意需要约分至最简分数），
输出积在原表的第几列第几行（若积形如 a（即结果为整数）或者 1/a，则看作表内的 a/1 或 1/a 结算）。

输入格式
共两行。每行输入一个分数（不一定是最简分数）。

输出格式
两个整数，表示输入的两个分数的积在表中的第几列第几行。

输入
4/5 5/4

输出
1 1
"""

# from math import gcd
#
# a = list(input().split('/'))
# b = list(input().split('/'))
#
# lst = []
#
# gcd_a = gcd(int(a[0]),int(b[1]))
# result_a = int(int(a[0])/gcd_a)
# result_b = int(int(b[1])/gcd_a)
# a[0] = result_a
# b[1] = result_b
#
# gcd_b = gcd(int(b[0]),int(a[1]))
# end_a = int(int(a[1])/gcd_b)
# end_b = int(int(b[0])/gcd_b)
# a[1] = end_a
# b[0] = end_b
#
#
# row = a[0] * b[0]
# col = a[1] * b[1]
# lst.append(col)
# lst.append(row)
#
# result = ' '.join(map(str,lst))
# print(result)


#gcd:最大公约数  lcm:最小公倍数
from math import gcd,lcm
# 最小公倍数=两数相乘÷两数的最大公约数

# 读取两个分数
frac1 = input().strip()
frac2 = input().strip()

# 解析分子分母
p1, q1 = map(int, frac1.split('/'))
p2, q2 = map(int, frac2.split('/'))

# 乘积
num = p1 * p2
den = q1 * q2

# 约分
g = gcd(num, den)
num //= g
den //= g

# 输出：第 den 行，第 num 列
print(den, num)