# 输入：2436 54  输出：[2436, 54]
a, b = list(map(int, input().split()))  # 1 2(赋值给a，b)
c = list(map(int, input().split()))
print(a, b)  # 1 2
print(c)  # [1, 2]



# 输入：abcde 输出：['a', 'b', 'c', 'd', 'e']
lis1 = list(input().strip())
print(lis1)



# 字符串转列表
s = "1 2 3"
lst = list(map(int, s.split()))  # [1, 2, 3]
print(lst)



# 列表推导式：在一行内完成for循环
squares = [i ** 2 for i in range(1, 6) if i > 2]  # 前面为执行的内容，中间for循环，结尾加入判断
print(squares)



# 列表转字符串
sl1 = [1, 2, 3]
sl2 = ' '.join(map(str, sl1))
print(sl2)  # 1 2 3




# 整型数转列表
def int_to_digits(n: int) -> list[int]:
    return [int(c) for c in str(n)]

s1 = 16
result = [int(c) for c in str(s1)]
print(result)  # [1,6]



# 直接在列表的最后一位上改变加1
l = [1, 2, 3]
l[-1] += 1
print(l)



# lambda表达式
nums = [1, 2, 3]
result = list(map(lambda x: x ** 2, nums))
print(result)  # [1, 4, 9]



# 过滤条件
numbers = [1, 2, 3, 4]
end = list(filter(lambda x: x % 2 == 0, numbers))
print(end)  # [2 , 4]



from functools import reduce
# 找最大值
max_num = reduce(lambda x, y: x if x > y else y, [3, 7, 2, 9, 1])
# 结果: 9



# 同时获取索引和值
fruits = ['apple', 'banana', 'orange']
for i, fruit in enumerate(fruits):
    print(f"{i}: {fruit}")



# 去除指定字符
text2 = "***hello***"
print(text2.strip('*'))  # "hello"



"--------------------------------------------------------------------------------------"


s = "A man, a plan, a canal: Panama"
# lis = list(s.split(','))  # 只能按逗号的位置分割
ls = list(s.strip())  # 不行

print(ls)



s = "A man, a plan, a canal: Panama"

# 方法1: 使用列表推导式筛选
cleaned = [char.lower() for char in s if char.isalnum()]
cleaned_str = ''.join(cleaned)
print(cleaned_str)  # 输出: amanaplanacanalpanama

# 方法2: 使用filter过滤
cleaned = filter(lambda x: x.isalnum(), s.lower())
cleaned_str = ''.join(cleaned)
print(cleaned_str)  # 输出: amanaplanacanalpanama



# 检查回文
print(cleaned_str == cleaned_str[::-1])  # 输出: True



# list.sort()为原地排序列表
list.sort()
# result=sorted(list)返回一个新列表，不改变原列表
result = sorted(list)

# isalnum()检查是否为字母和数字组成
# isalpha()检查是否为字母组成
# isdigit()检查是否为数字组成
# islower()检查是否为小写   # 转换大小写为upper()和lower()
# isupper()检查是否为大写