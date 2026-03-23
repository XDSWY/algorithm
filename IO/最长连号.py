"""
10
1 5 6 2 3 4 5 6 8 9

数出其中最长的连号数
"""
n = int(input())
ai = list(map(int,input().split()))

tot, result = 0,0


for i in range(n):
    if ai[i-1] == ai[i] - 1:
        tot += 1
        if tot > result:
            result = tot
    else:
        tot = 0

print(result+1)