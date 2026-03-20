N = int(input())
nums = []

for i in range(1,N+1):
    if i % 2026 == 0:
        nums.append(i)
    elif str("2026") in str(i):
        nums.append(i)

result = ' '.join(map(str, nums))
print(result)