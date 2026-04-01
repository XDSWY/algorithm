"""
题目描述
于是，小W便在搭讪大神的同时，也关注着电梯中显示的楼层数字，并且他注意到电梯每向上运行一层需要 6 秒钟，
向下运行一层需要 4 秒钟，每开门一次需要 5 秒（如果有人到达才开门），并且每下一个人需要加 1 秒。
特别指出，电梯最开始在 0 层，并且最后必须再回到 0 层才算一趟任务结束。
假设在开始的时候已知电梯内的每个人要去的楼层，你能计算出完成本趟任务需要的总时间吗?

输入格式
共 2 行 第 1 行，一个正整数 n，表示乘坐电梯的人数。 第 2 行，n 个正整数，ai表示第 i 个人要去的楼层。

输出格式
仅 1 行，一个正整数，表示完成这趟任务需要的时间。

输入
4
2 4 3 2

输出
59
"""

n = int(input())
floor = list(map(int, input().split()))
open = 5

sort_floors = sorted(set(floor))

# count = {}
# for f in floors:
#     if f in count:
#         count[f] += 1
#     else:
#         count[f] = 1

count = {}
for i in floor:
    count[i] = count.get(i, 0) + 1

time = 0
current = 0

for i in sort_floors:
    if i > current:
        time += (i - current) * 6
    else:
        time += (current - i) * 4
    time += open
    time += count[i]
    current = i

if sort_floors[-1] != 0:
    time += sort_floors[-1] * 4

print(time)
