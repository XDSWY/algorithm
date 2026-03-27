"""
10 2
"""
# x, n = list(map(int,input().split()))
# sum, first, last  = 0, 1, 0
#
# for i in range(n):
#     first= first + sum + last
#     sum = (sum + last + first) * 10
#
# print(sum)


x, n = map(int, input().split())
total = 1

for i in range(n):
    total += total * x

print(total)

