n = 8
s = "r11CA2aS"


string = list(s.strip())
for i in range(n):
    if string[i].isupper():
        string[i] = string[i].lower()
    elif string[i].islower():
        string[i] = string[i].upper()

upper = 0
lower = 0
number = 0


for i in string:
    if i.isupper():
        upper += 1
    elif i.islower():
        lower += 1
    elif i.isdigit():
        number += 1

result = ''.join(string)
print(result)
print(f"{upper} {lower} {number}")