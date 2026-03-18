"""
小组名和彗星名都以下列方式转换成一个数字：最终的数字就是名字中所有字母的积，其中 A 是 1，Z 是 26。例如，USACO 小组就是 21×19×1×3×15=17955。
如果小组的数字 mod47 等于彗星的数字 mod47，你就得告诉这个小组需要准备好被带走！（记住“amodb”是 a 除以 b 的余数，例如 34mod10 等于 4）
写出一个程序，读入彗星名和小组名并算出用上面的方案能否将两个名字搭配起来，如果能搭配，就输出 GO，否则输出 STAY。
小组名和彗星名均是没有空格或标点的一串大写字母（不超过 6 个字母）。

输入格式
第 1 行：一个长度为 1 到 6 的大写字母串，表示彗星的名字。
第 2 行：一个长度为 1 到 6 的大写字母串，表示队伍的名字。
输出格式
无
输入输出样例
输入
COMETQ
HVNGAT
输出
GO

输入
ABSTAR
USACO
输出
STAY
"""
star = str(input())
group = str(input())
star_num, group_num = 1, 1

for i in star:
    star_num *= ord(i) - 64

for j in group:
    group_num *= ord(j) - 64

if star_num % 47 == group_num % 47:
    print("GO")
else:
    print("STAY")



