Pascal = list(map(str,input().strip()))
print(Pascal)

lst = [0,0,0]

for i in range(len(Pascal)-4):
    if Pascal[i] == 'a':
        if Pascal[i+3] == 'b':
            lst[0] = lst[1]
        elif Pascal[i+3] == 'c':
            lst[0] = lst[2]
        elif Pascal[i+3] == 'a':
            lst[0] = lst[0]
    else:
        lst[0] = Pascal[i+3]
        print(lst[0])

    if  Pascal[i] == 'b':
        if Pascal[i+3] == 'a':
            lst[1] = lst[0]
        elif Pascal[i+3] == 'c':
            lst[1] = lst[2]
        elif Pascal[i+3] == 'b':
            lst[1] = lst[1]
    else:
        lst[1] = Pascal[i+3]

    if Pascal[i] == 'c':
        if Pascal[i+3] == 'a':
            lst[2] = lst[0]
        elif Pascal[i+3] == 'b':
            lst[2] = lst[1]
        elif Pascal[i+3] == 'c':
            lst[2] = lst[2]
    else:
        lst[2] = Pascal[i+3]

result=' '.join(map(str,lst))
print(result)

