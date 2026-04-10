import os
import sys

first, second, third = 5, 0, 0
tot = 2025
i = 0

while tot > 0:
    i += 1
    if i % 2 == 0:
        second = 2
    else:
        second = 15

    if i % 3 == 1:
        third = 2
    elif i % 3 == 2:
        third = 10
    elif i % 3 == 0:
        third = 7

    result = first + second + third
    print(i,result)

    tot -= result
    print(i,tot)

    if tot <= 0:
        print(i)
        break




