# 判断素数
import math

n =int(input())

def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False

    max_divisor = int(math.sqrt(n))+1

    for i in range(3, max_divisor, 2):
        if n % i == 0:
            return False
    return True

# print(is_prime(3))

list = []
for i in range(2, n+1):
    if is_prime(i):
        list.append(i)
print(list)


nums = []
for i in range(2, n+1):
    if i*2 <= n:
        nums.append(i*2)

tot = 0
print(nums)

for num in nums:
    found = False
    for i in list:
        if i > num//2:
            break
        p2 = num - i
        if p2 in list:
            print(f"{num}+{i}+{p2}")
        tot += i
        found = True
        break
