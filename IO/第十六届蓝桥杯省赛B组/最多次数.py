"""
小蓝有一个字符串 s，他特别喜欢由以下三个字符组成的单词：
l,q,b,任意顺序都可以，一共有6 种可能：
lqb、lbq、qlb、qbl、blq、bql。
现在他想从s 中，尽可能切割出多个他喜欢的单词，请问最多能切割出多少个？单词指的是由若干个连续的字符组成的子字符串。

输入格式
输入一行包含一个字符串s。

输出格式
输出一行包含一个整数表示答案。

样例输入
lqbblqblqlxqb

样例输出
3
"""

# s = list(input().strip())
# result = 0
#
# print(s)
# i = 0
#
# while i < len(s) - 2:
#     # 统一用一个 if-elif-else 结构
#     if s[i] == 'l':
#         if s[i+1] == 'q' and s[i+2] == 'b':
#             result += 1
#             i += 3
#         elif s[i+1] == 'b' and s[i+2] == 'q':
#             result += 1
#             i += 3
#         else:
#             i += 1
#     elif s[i] == 'q':
#         if s[i+1] == 'l' and s[i+2] == 'b':
#             result += 1
#             i += 3
#         elif s[i+1] == 'b' and s[i+2] == 'l':
#             result += 1
#             i += 3
#         else:
#             i += 1
#     elif s[i] == 'b':
#         if s[i+1] == 'l' and s[i+2] == 'q':
#             result += 1
#             i += 3
#         elif s[i+1] == 'q' and s[i+2] == 'l':
#             result += 1
#             i += 3
#         else:
#             i += 1
#     else:
#         i += 1
#
# print(result)


s = input().strip()
n = len(s)
result = 0
i = 0

words = {'lqb', 'lbq', 'qlb', 'qbl', 'blq', 'bql'}

while i <= n - 3:
    if s[i:i+3] in words:
        result += 1
        i += 3  # 切出一个单词，跳过3个字符
    else:
        i += 1  # 无法组成单词，往后移动一位

print(result)