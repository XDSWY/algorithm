"""
3
5 9
1 4
3 7
"""

N = int(input())
time = []

for i in range(N):
    start_time, end_time = map(int, input().split())
    time.append((start_time, end_time))

time.sort()

max_cover = 0

for i in range(N):
    # 类似于两个指针，每次循环同时向后移动一格
    remaining = time[:i] + time[i + 1:]

    if not remaining:
        cover = 0
    else:
        start_time, end_time = remaining[0]
        cover = 0
        for start, end in remaining[1:]:
            if start <= end_time:
                end_time = max(end_time, end)
            else:
                cover += end_time - start_time
                start_time, end_time = start, end
        cover += end_time - start_time

    if cover > max_cover:
        max_cover = cover

print(max_cover)



