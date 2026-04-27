"""
题目描述
在国家精密光学实验室中，研究员正利用两组高功率相干激光器进行 “量子干涉条纹” 锁定实验。
设 1 号激光器的输出功率为 a（0≤a≤20269876543210），2 号激光器的输出功率为 b（0≤b≤20260123456789），其中 a,b 均为非负整数。
物理规律表明，只有当系统总功率 S=a+b 恰好为一个完全平方数时，干涉条纹方可被成功锁定。
请问，一共有多少种不同的功率配给方案 (a,b) 能够使实验成功锁定？由于方案数可能很大，你只需要给出方案数对 998244353 取模后的结果即可。
注意：两个方案 (a1,b1)和(a2,b2) 被认为是不同的，当且仅当 a1≠a2或 b1≠b2。

输入格式
无

输出格式
这是一道结果填空题，你只需要算出结果后提交即可。本题的结果为一个整数，在提交答案时只填写这个整数，填写多余的内容将无法得分。
"""
import math

A = 20269876543210
B = 20260123456789
MOD = 998244353

sqrtB = math.isqrt(B)
sqrtA = math.isqrt(A)
sqrtAB = math.isqrt(A + B)

def sum_squares(a, b):
    if a > b: return 0
    def S(x):
        return x * (x + 1) * (2 * x + 1) // 6
    return S(b) - S(a - 1)

ans = 0

# 第一段：0 ≤ k ≤ sqrtB
cnt1 = sum_squares(0, sqrtB)       # Σ k²
ans = (cnt1 + (sqrtB + 1)) % MOD   # Σ 1 → sqrtB+1 项

# 第二段：sqrtB+1 ≤ k ≤ sqrtA
len2 = max(0, sqrtA - sqrtB)
if len2 > 0:
    ans = (ans + len2 * (B + 1)) % MOD

# 第三段：sqrtA+1 ≤ k ≤ sqrtAB
len3 = max(0, sqrtAB - sqrtA)
if len3 > 0:
    # Σ (A+B+1 - k²)
    total_sum_k2 = sum_squares(sqrtA + 1, sqrtAB)
    cnt3 = len3 * (A + B + 1) - total_sum_k2
    ans = (ans + cnt3) % MOD

print(ans)









# # 因为 a+b = k² ≤ A+B，所以 k ≤ √(A+B)
# maxK = int((A + B) ** 0.5)
# # 如果 (maxK+1)² 仍然 ≤ A+B，说明 maxK 算小了
# while (maxK + 1)*(maxK + 1) <=  A + B:
#     maxK += 1
#
# tot = 0 # 总个数
#
# for k in range(maxK + 1):
#     s = k * k   # 当前的平方数
#
#     # 由 b = s - a，且 0 ≤ b ≤ B，得：
#     #   0 ≤ s - a ≤ B
#     #   s - B ≤ a ≤ s
#     # 再加上 a 本身的限制：0 ≤ a ≤ A
#     # 所以 a 的范围是：[max(0, s-B), min(A, s)]
#     low = s - B
#     if low < 0:
#         low = 0
#
#     high = s
#     if high > A:
#         high = A
#
#     # 如果 low ≤ high，说明存在有效的a,计算a的区间范围
#     if low <= high:
#         cnt = high - low + 1  # a 有多少种取值，就有多少对 (a,b)
#         tot += cnt
#
# print(tot % MOD)







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
