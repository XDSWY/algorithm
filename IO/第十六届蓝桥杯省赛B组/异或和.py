import os
import sys

n = int(input())
integer = list(map(int, input().split()))
result = 0

for i in range(n):
  for j in range(i+1, n):
    result += (integer[i] ^ integer[j]) * (j - i)

print(result)
