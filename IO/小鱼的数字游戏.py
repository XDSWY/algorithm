"""
反向输出，若第一位为0时，则省略
输入输出样例
输入
3 65 23 5 34 1 30 0

输出
30 1 34 5 23 65 3
"""

n = list(map(int,input().split()))
result = n[::-1]

if result[0] == 0:
    result.remove(result[0])

end = ' '.join(map(str,result))
print(end)
