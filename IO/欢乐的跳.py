"""
一个 n 个元素的整数数组，如果数组两个连续元素之间差的绝对值包括了 [1,n−1] 之间的所有整数，
则称之符合“欢乐的跳”，如数组 {1,4,2,3} 符合“欢乐的跳”，因为差的绝对值分别为：3,2,1。
给定一个数组，你的任务是判断该数组是否符合“欢乐的跳”。
输入格式
每组测试数据第一行以一个整数 n(1≤n≤1000) 开始，接下来 n 个空格隔开的在 [−10的8次方,10的8次方] 之间的整数。
输出格式
对于每组测试数据，输出一行若该数组符合“欢乐的跳”则输出 Jolly，否则输出 Not jolly。

输入输出样例
输入
4 1 4 2 3
输出
Jolly

输入
5 1 4 2 -1 6
输出
Not jolly
"""

n = list(map(int, input().split()))
nums = []

for i in range(2, len(n)):
    if n[i - 1] - n[i] < 0:
        result = n[i] - n[i - 1]
        nums.append(result)
    else:
        result = n[i - 1] - n[i]
        nums.append(result)

end = []
for j in range(1, n[0]):
    end.append(j)


nums.sort()
end.sort()

if nums == end:
    print("Jolly")
else:
    print("Not jolly")







