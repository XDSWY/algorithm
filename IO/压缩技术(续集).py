"""
题目描述
设某汉字由 N×N 的 0 和 1 的点阵图案组成。
我们依照以下规则生成压缩码。连续一组数值：从汉字点阵图案的第一行第一个符号开始计算，按书写顺序从左到右，由上至下。
第一个数表示连续有几个 0，第二个数表示接下来连续有几个 1，第三个数再接下来连续有几个 0，第四个数接着连续几个 1，以此类推……

例如: 以下汉字点阵图案：
0001000
0001000
0001111
0001000
0001000
0001000
1111111
对应的压缩码是： 7 3 1 6 1 6 4 3 1 6 1 6 1 3 7 （第一个数是 N，其余各位表示交替表示 0 和 1 的个数，压缩码保证 N×N= 交替的各位数之和）
输入输出样例
输入
0001000
0001000
0001111
0001000
0001000
0001000
1111111

输出
7 3 1 6 1 6 4 3 1 6 1 6 1 3 7
"""

nums = []

row = list(map(str, input().strip()))
nums += row

for i in range(len(row)-1):
    col = list(map(str, input().strip()))
    nums += col

result = []
result.append(len(row))

count_0, count_1 = 0,0
current = nums[0]

if nums[0] == '1':
    result.append('0')

for i in range(len(nums)):

    if nums[i] == '0':
        if current == '1':
            result.append(count_1)
            count_1 = 0
            current = '0'
        count_0 += 1

    elif nums[i] == '1':
        if current == '0':
            result.append(count_0)
            count_0 = 0
            current = '1'
        count_1 += 1


if count_0 > 0:
    result.append(count_0)
elif count_1 > 0:
    result.append(count_1)

print(' '.join(map(str, result)))

