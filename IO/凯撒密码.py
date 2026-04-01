"""
题目描述
蒟蒻虽然忘记密码，但他还记得密码是由一个字符串组成。
密码是由原文字符串（由不超过 50 个小写字母组成）中每个字母向后移动 n 位形成的。
z 的下一个字母是 a，如此循环。他现在找到了移动前的原文字符串及 n，请你求出密码。

输入格式
第一行：n。第二行：未移动前的一串字母。

输出格式
一行，是此蒟蒻的密码。

输入
1
qwe

输出
rxf
"""

n = int(input())
pwd = list(map(str, input().strip()))

for i in range(len(pwd)):
    nums = ord(pwd[i])
    nums += n
    if nums > 122:
        nums = (nums - 122) + 96
    pwd[i] = chr(nums)

result = ''.join(map(str, pwd))
print(result)

