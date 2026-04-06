"""
题目描述
在 DNF 中，赵神牛有一个缔造者，他一共有 k 点法力值，一共有 m 个技能，每个技能耗费的法力值为 a i，可以造成的伤害为 b i
，而 boss 的体力值为 n，请你求出它放哪个技能，才可以打死 boss。
当然，赵神牛技术很菜，他一局只放一个技能，不过每个技能都可以放无数次。

输入格式
第一行有三个整数，分别表示 k,m,n。
后面 m 行，每行两个整数，第 (i+1) 行的整数表示耗费的法力值 ai和造成的伤害bi。

输出格式
输出仅一行，即可以杀死 boss 的技能序号，如果有多个，按从小到大的顺序输出，中间用一个空格隔开；如果没有技能能杀死 boss，输出 -1。

输入
100 3 5000
20 1000
90 1
110 10000

输出
1

输入
50 4 10
60 100
70 1000
80 1000
90 0

输出
-1
"""

k, m, n = map(int, input().split())
integer = 0
lst = []

for i in range(m):
    ai, bi = map(int, input().split())
    if ai == 0:
        if bi >= 0:
            lst.append(i + 1)
        continue

    integer = k // ai
    if integer * bi >= n:
        lst.append(i + 1)

if len(lst) == 0:
    print('-1')
else:
    print(' '.join(map(str, lst)))


