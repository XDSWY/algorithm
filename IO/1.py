n = int(input())
s = str(input())

digit = []
lower = []
upper = []

lst = list(s.strip())
for i in range(len(lst)):
    if lst[i].isdigit():
        digit.append((lst[i]))
    elif lst[i].islower():
        lower.append((lst[i]))
    elif lst[i].isupper():
        upper.append((lst[i]))

result = ''.join(digit+lower+upper)


