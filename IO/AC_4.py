#5 4
#5 7 15 20 11
#58 85 50 49
#9 11 9 4
#7 12 5 9

n, m = map(int, input().split())

# 我方兵力
mine = list(map(int, input().split()))

# 敌方下策兵力
rear = list(map(int, input().split()))
# 敌方中策兵力
mid = list(map(int, input().split()))
# 敌方上策兵力
front = list(map(int, input().split()))


result_front = 0
result_mid = 0
result_rear = 0

# 下策
new_mine_rear = [0]*n

for j in range(len(mine)):
    new_mine_rear[j] = mine[j] + 15

if sum(new_mine_rear) > sum(rear):
    result_rear = sum(new_mine_rear) - sum(rear)


# 中策
if sum(mine) > sum(mid):
    result_mid = sum(mine) - sum(mid)

# 上策
new_mine_front = [0]*n

for k in range(len(mine)):
    new_mine_front[k] = mine[k] - 10
    if new_mine_front[k] < 0:
        new_mine_front[k] = 0

new_front = [0]*m
for i in range(len(front)):
    new_front[i] = int(front[i] / 3)

# result
if sum(new_mine_front) > sum(new_front):
    result_front = sum(new_mine_front) - sum(new_front)


if max(result_front,result_mid,result_rear) > 0:
    print(max(result_front,result_mid,result_rear))
else:
    print("helpless")





