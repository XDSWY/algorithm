"""
5
1 2
2 1
3 6
1000000000000000000 1000000000000000000
172635817456 237896190123
"""
# from math import gcd
#
# found = False
#
# T = int(input())
# for i in range(T):
#     a, b = map(int, input().split())
#     for x in range(1,(10**18)+1):
#         if gcd(a, x) == 1 and gcd(b, x) > 1:
#             print(x)
#             found = True
#             break
#
# if not found:
#     print(-1)

from math import gcd

def solve():
    T = int(input())
    for _ in range(T):
        a, b = map(int, input().split())

        if b == 1:
            print(-1)
            continue

        if gcd(a, b) == 1:
            print(b)
            continue

        # 找 b 的一个质因数 p，且 p 不整除 a
        x = -1
        tb = b
        p = 2
        while p * p <= tb:
            if tb % p == 0:
                if a % p != 0:
                    x = p
                    break
                while tb % p == 0:
                    tb //= p
            p += 1
        if x == -1 and tb > 1 and a % tb != 0:
            x = tb

        print(x)


if __name__ == "__main__":
    solve()

