A = 20269876543210
B = 20260123456789
MOD = 988765432

# 因为 a+b = k² ≤ A+B，所以 k ≤ √(A+B)
maxK = int((A + B) ** 0.5)
# 如果 (maxK+1)² 仍然 ≤ A+B，说明 maxK 算小了
while (maxK + 1)*(maxK + 1) <=  A + B:
    maxK += 1

tot = 0 # 总个数

for k in range(maxK + 1):
    s = k * k   # 当前的平方数

    # 由 b = s - a，且 0 ≤ b ≤ B，得：
    #   0 ≤ s - a ≤ B
    #   s - B ≤ a ≤ s
    # 再加上 a 本身的限制：0 ≤ a ≤ A
    # 所以 a 的范围是：[max(0, s-B), min(A, s)]
    low = s - B
    if low < 0:
        low = 0

    high = s
    if high > A:
        high = A

    # 如果 low ≤ high，说明存在有效的a,计算a的区间范围
    if low <= high:
        cnt = high - low + 1  # a 有多少种取值，就有多少对 (a,b)
        tot += cnt

print(tot % MOD)


# s = 0
# A = 20269876543210
# B = 20260123456789
# MOD = 988765432
#
# for i in range(A+1):
#     for j in range(B+1):
#         s = i + j
#         number = s ** (1 / 2)
#         if number == int(number):
#             tot += 1
#
# result = tot % MOD
# print(result)
