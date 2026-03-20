"""
3 4
10 20 30
15 25 35 5
"""
N, M = list(map(int, input().split()))

require = list(map(int, input().split()))
supply = list(map(int, input().split()))


require.sort()
supply.sort()

matched = 0
total_used = 0
used = [False] * M


for i in range(N):
    best_match = -1
    min = float('inf')


    for j in range(M):
        if not used[j] and supply[j] >= require[i]:
            result = supply[j] - require[i]
            if result < min:
                min = result
                best_match = j

    if best_match != -1:
        used[best_match] = True
        matched += 1
        total_used += supply[best_match]

print(f"{matched}")
print(f"{total_used}")