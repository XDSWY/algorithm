s = input().strip()
a, b, c = 0, 0, 0

statements = s.split(';')

for i in statements:
    if not i.strip():
        continue

    if ':=' in i:
        left, right = i.split(':=')
        left = left.strip()
        right = right.strip()

        if right.isdigit():
            val = int(right)
        elif right in ['a', 'b', 'c']:
            val = eval(right)   # eval() 是 Python 的一个内置函数，用于将字符串当作 Python 代码执行。
        else:
            continue

        if left == 'a':
            a = val
        elif left == 'b':
            b = val
        elif left == 'c':
            c = val

print(a, b, c)