"""
例如，五位数 20207 可以拆分成
sub 1=202
sub 2=020 (=20)
sub 3=207

现在给定一个正整数 K，要求你编程求出 10000 到 30000 之间所有满足下述条件的五位数，
条件是这些五位数的三个子数都可被 K 整除。
输入格式
一个正整数 K。
输出格式
每一行为一个满足条件的五位数，要求从小到大输出。不得重复输出或遗漏。如果无解，则输出 No。
"""
K = int(input())
result = []
# found=False

for i in range(10000, 30001):
    if (i // 100) % K == 0 and (i % 1000) % K == 0 and (i % 10000 // 10) % K == 0:
        print(i)
        # found=True
        result.append(i)

# if not found:
if len(result) == 0:
    print('No')


