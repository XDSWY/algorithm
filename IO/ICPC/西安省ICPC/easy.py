n = int(input())

# 选中的格子集合
selected = set()

# 先选每行的前两个（第0行和第1列）
for i in range(n):
    selected.add((i, 0))
    selected.add((i, 1))

# 列计数
col_cnt = [0]*n
for i, j in selected:
    col_cnt[j] += 1

# 把超出2的列的上方大数去掉，换到不足2的列
need = [i for i in range(n) if col_cnt[i] < 2]
extra = [i for i in range(n) if col_cnt[i] > 2]

for ex in extra[:]:
    if col_cnt[ex] > 2:
        for i in range(n-1, -1, -1):
            if (i, ex) in selected and col_cnt[ex] > 2:
                selected.remove((i, ex))
                col_cnt[ex] -= 1
                if need:
                    j = need.pop(0)
                    selected.add((i, j))
                    col_cnt[j] += 1
                    if col_cnt[j] == 2:
                        need = [x for x in range(n) if col_cnt[x] < 2]

# 计算总和
ans = 0
for i, j in selected:
    ans += i*n + j + 1
print(ans)