N, M = map(int, input().split())
a = N // M      # 每个数至少这么大
b = N % M       # 有 b 个数需要再加 1

# 前 M-b 个数是 a，后 b 个数是 a+1
result = [a] * (M - b) + [a + 1] * b
print(' '.join(map(str, result)))