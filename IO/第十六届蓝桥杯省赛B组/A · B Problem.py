import os
import sys

L = int(input())

result = 0

for i in range(1, L):
    x1 = i
    for j in range(1, L):
        x2 = j
        for k in range(1, L):
            y1 = k
            for l in range(1, L):
                y2 = l
                if (x1 * x2) + (y1 * y2) <= L:
                    result += 1

print(result)

