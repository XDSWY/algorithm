"""
题目描述
请统计某个给定范围 [L,R] 的所有整数中，数字 2 出现的次数。
比如给定范围 [2,22]，数字 2 在数 2 中出现了 1 次，在数 12 中出现 1 次，在数 20 中出现 1 次，在数 21 中出现 1 次，在数 22 中出现 2 次，
所以数字 2 在该范围内一共出现了 6 次。

输入格式
2 个正整数 L 和 R，之间用一个空格隔开。

输出格式
数字 2 出现的次数。
"""
# L,R  = map(int,input().split())
# result = 0

# for i in range(L,R+1):
    # nums = [int(j) for j in str(i)]
    # for k in nums:
        # if k == 2:
           #  result += 1
# print(result)

l, r = list(map(int, input().split()))
count = 0
for i in range(l, r + 1):
    count+=str(i).count('2')   # 统计字符串2
print(count)

