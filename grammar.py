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

# 正常写法
# cleaned = []
# for char in s:
#     if char.isalnum():
#         cleaned.append(char.lower())
# cleaned_str = ''.join(cleaned)




# 方法2: 使用filter过滤
cleaned = filter(lambda x: x.isalnum(), s.lower())   # 会返回一个只包含字母和数字的小写字符的迭代器
cleaned_str = ''.join(cleaned)
print(cleaned_str)  # 输出: amanaplanacanalpanama

# 正常写法
# cleaned = []
# for char in s.lower():
#     if char.isalnum():
#         cleaned.append(char)
# cleaned_str = ''.join(cleaned)


"--------------------------------------------------------------------------------------"
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

"----------------------------------------------------------------------------"
#gcd:最大公约数  lcm:最小公倍数
from math import gcd,lcm
# 最小公倍数=两数相乘÷两数的最大公约数

def gcd(a, b):
    while b != 0:
        a, b = b, a % b  # 替换 a 和 b，b 变成余数
    return a  # 当 b 为 0 时，a 就是最大公约数

def lcm(a, b):
    return abs(a * b) // gcd(a, b)  # 用 GCD 求 LCM

"---------------------------------------------------------------------------------"
a = 9
b = 4

result = a % b # 取余
print(result)  # 输出: 1

result = a / b # 浮点除法
print(result)  # 输出: 2.25

result = a // b # 整数除法(舍去小数)
print(result)  # 输出: 2

"----------------------------------------------------------------------------------"
pairs = [(1, 'apple'), (2, 'banana'), (3, 'cherry')]

# 使用 enumerate 遍历索引和元组中的元素
for i, (a, b) in enumerate(pairs):
    print(f"索引 {i}, a: {a}, b: {b}")
# 索引 0, a: 1, b: apple
# 索引 1, a: 2, b: banana
# 索引 2, a: 3, b: cherry



# 普通列表
numbers = [1, 2, 3]
# 正确写法
for i, a in enumerate(numbers):
    print(f"索引 {i}, a: {a}")
# 索引 0, a: 1
# 索引 1, a: 2
# 索引 2, a: 3

"----------------------------------------------------------------------------"
numbers = [1, 2, 3, 4, 5]

# 使用 zip() 来获取相邻元素
for a, b in zip(numbers, numbers[1:]):
    print(f"比较 {a} 和 {b}")
# 比较 1 和 2
# 比较 2 和 3
# 比较 3 和 4
# 比较 4 和 5

"------------------------------------------------------------------------------"
numbers = [1, 2, 3, 4, 5]

# 使用索引比较相邻元素，最后一个元素和第一个元素也进行比较0
for i in range(len(numbers)):
    print(f"比较 {numbers[i]} 和 {numbers[(i + 1) % len(numbers)]}")
# 比较 1 和 2
# 比较 2 和 3
# 比较 3 和 4
# 比较 4 和 5
# 比较 5 和 1