"""
题目描述
小 a 和 uim 喜欢互相切磋三子棋。三子棋大家都玩过是吗？就是在九宫格里面 OOXX（别想歪了），谁连成 3 个就赢了。
由于小 a 比较愚蠢，uim 总是让他先。
我们用 9 个数字表示棋盘位置：
1 2 3
4 5 6
7 8 9
所有的棋谱都是已经结束的棋局，要么一方获胜，要么平局。
今天，他们下了一下午的棋，小 a 为了提高技术，录下了很多棋谱。他想知道，一盘棋结束时，到底是谁赢。

输入格式
一行，一串数字，表示落子的地点。小 a 总是先下。

输出格式
一行，如果小 a 赢，输出 xiaoa wins.。如果 uim 赢，输出 uim wins.。如果平局，输出 drew.。

输入输出样例
输入
5237649
输出
xiaoa wins.

输入
539128647
输出
drew.

"""
# position = list(map(int,input().strip()))
#
# position.sort()
# found = False
#
# if len(position) == 9:
#     found = True
#     print("drew.")
#
# for i in range(len(position) - 2):
#     if not found:
#         if position[i] + 1 == position[i + 1] and position[i + 1] + 1== position[i + 2]:
#             print("xiaoa wins.")
#             break
#         elif [1, 5 ,9] in position or [3 ,5 ,7] in position:
#             print("xiaoa wins.")
#             break
#         elif [1, 4, 7] in position or [2, 5, 8] in position or [3, 6, 9] in position:
#             print("xiaoa wins.")
#             break
#         else:
#            print("uim wins.")
#     else:
#         break


# 整个棋局过程中是否有人成线，而不是只在结束时判断。
position = list(map(int, input().strip()))

xiaoa = position[::2]
uim = position[1::2]

together_combination = []

row = []
for i in range(3):
    num = i * 3 + (i + 1)
    row.append(num)

rol = []
for i in range(3):
    num = (i + 1) * 3 - i
    rol.append(num)

for i in range(1, 10, 3):
    horizontal = [i, i + 1, i + 2]
    together_combination.append(horizontal)

for j in range(1, 4):
    vertical = [j, j + 3, j + 6]
    together_combination.append(vertical)

together_combination.append(row)
together_combination.append(rol)

win = False
winner = None

for step in range(1, len(position) + 1):
    current = position[:step]

    current_xiaoa = current[::2]
    current_uim = current[1::2]

    for comb in together_combination:
        if all(num in current_xiaoa for num in comb):
            win = True
            winner = "xiaoa"
            break

    if not win:
        for comb in together_combination:
            if all(num in current_uim for num in comb):
                win = True
                winner = "uim"
                break
    if win:
        break

if win:
    print(f"{winner} wins.")
else:
    print("drew.")