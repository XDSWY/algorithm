# 敌方上策兵力
front = list(map(int, input().split()))

new_front = front
for i in range(len(front)):
    new_front[i] = int(front[i] / 3)
print(new_front)