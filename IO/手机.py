"""
题目描述
一般的手机的键盘是这样的：
要按出英文字母就必须要按数字键多下。例如要按出 x 就得按 9 两下，第一下会出 w，而第二下会把 w 变成 x。0 键按一下会出一个空格。
你的任务是读取若干句只包含英文小写字母和空格的句子，求出要在手机上打出这个句子至少需要按多少下键盘。
输入格式
一行句子，只包含英文小写字母和空格，且不超过 200 个字符。
输出格式
一行一个整数，表示按键盘的总次数。

输入
i have a dream

输出
23
"""

string = list(map(str,input()))
print(string)
sum = 0
lst_1 = []
lst_2 = []
lst_3 = []
lst_4 = []

for i in range(97, 112, 3):
    lst_1.append(i)
    lst_2.append(i + 1)
    lst_3.append(i + 2)

for i in range(112, 116, 4):
    lst_1.append(i)
    lst_2.append(i + 1)
    lst_3.append(i + 2)
    lst_4.append(i + 3)

for i in range(116, 119, 3):
    lst_1.append(i)
    lst_2.append(i + 1)
    lst_3.append(i + 2)


for i in range(119, 123, 4):
    lst_1.append(i)
    lst_2.append(i + 1)
    lst_3.append(i + 2)
    lst_4.append(i + 3)


for i in string:
    if i == " ":
        sum += 1
    elif ord(i) in lst_1:
        sum += 1
    elif ord(i) in lst_2:
        sum += 2
    elif ord(i) in lst_3:
        sum += 3
    elif ord(i) in lst_4:
        sum += 4

print(sum)

