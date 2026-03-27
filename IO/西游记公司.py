"""
输入格式
第一行：一个时间，为 时：分：秒 形式，表示猪八戒打算去偷沙和尚笔记本的时间；
第二行：一个时间，为 时：分：秒 形式，表示孙悟空打算去偷猪八戒平底锅的时间。
注：时间可能有前导零，也有可能没有。
第三行：一行一个整数 n，表示猪八戒一秒能偷沙和尚的笔记本数。
保证第一行的时间要比第二行的时间早。

输出格式
一个整数，表示猪八戒能偷沙和尚笔记本的个数。

输入
00:0:00
0:00:10
10

输出
100
"""
time_zhu = input().split(":")
time_sun = input().split(":")
n = int(input())

hour, minute, second = 0, 0, 0
hour = ((int(time_sun[0])-int(time_zhu[0]))*3600)*n
minute = ((int(time_sun[1])-int(time_zhu[1]))*60)*n
second = (int(time_sun[2])-int(time_zhu[2]))*n

sum = hour + minute + second
print(sum)
