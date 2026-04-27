




# import sys
# from string import digits
#
# sys.set_int_max_str_digits(10000)
#
# lst = []
# number, tot = 0, 0
#
#
# for i in range(1, 2027):
#     lst.append(i)
#     number = ''.join(map(str, lst))
#     if int(number) % 26 == 0:
#         tot += 1
#
# print(tot)

tot = 0
remainder = 0

for i in range(1, 2027):
    digits = len(str(i))
    power = 10 ** digits
    remainder = (remainder *power + i) % 26  # 上一位的数字的余数乘以下一位数字的位数，再加下一位数字，拼接后数字的去除26，即为余数
    if remainder == 0:
        tot += 1

print(tot)


