"""
题目描述
幸运机会是一种彩票游戏。每张彩票都有一个游戏区域和一个刮刮区。游戏区域是一个 r×c 的矩形区域，
填满了数字。刮刮区隐藏了指定投注单元格的行号和列号。

有四种可能的获胜方向：上、下、左和右。如果从投注单元格开始的某个方向上的所有数字都严格小于投注单元格中的数字，
那么你就赢得了这个方向。如果投注单元格位于网格的边缘，你将自动赢得相应的方向！
拉里想选择一张在所有可能的投注单元格中获胜方向总数最多的票。编写一个程序来确定给定网格的这个数字。

输入格式
输入文件的第一行包含两个整数 r 和 c —— 网格中的行数和列数 (1≤r,c≤100)。

接下来的 r 行每行包含 c 个整数 —— 网格上打印的数字。每个数字都是正数且不超过 1000。

输出格式
输出一个整数 w —— 给定网格的获胜方向总数。

输入
3 4
5 3 9 10
1 8 8 2
4 3 4 3

输出
25
"""
r, c = map(int, input().split())
nums = [list(map(int, input().split())) for _ in range(r)]
# nums = []
# for i in range(r):
#     nums.append(lst[i])

print(nums)
# 上方
up = [ [0] * c for _ in range(r)]
for i in range(c):
    for j in range(1, r):
        up[j][i] = max(up[j - 1][i], nums[j - 1][i])

# 下方
down = [ [0] * c for _ in range(r)]
for i in range(c):
    for j in range(r - 2, -1, -1):
        down[j][i] = max(down[j + 1][i], nums[j + 1][i])

# 左方
left = [ [0] * c for _ in range(r)]
for i in range(r):
    for j in range(1, c):
        left[i][j] = max(left[i][j - 1], nums[i][j - 1])

# 右方
right = [ [0] * c for _ in range(r)]
for i in range(r):
    for j in range(c - 2, -1, -1):
        right[j][i] = max(right[i][j + 1], nums[i][j + 1])

ans = 0
for i in range(r):
    for j in range(c):
        v = nums[i][j]
        win = 0
        if i == 0 or up[i][j] < v:
            win += 1
        if i == r - 1 or down[i][j] < v:
            win += 1
        if j == 0 or left[i][j] < v:
            win += 1
        if j == c - 1 or right[i][j] < v:
            win += 1
        ans += win

print(ans)