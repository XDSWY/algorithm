"""
题目描述
假设一个表达式有英文字母（小写）、运算符（+、-、*、/）和左右小（圆）括号构成，以 @ 作为表达式的结束符。
请编写一个程序检查表达式中的左右圆括号是否匹配，若匹配，则输出 YES；否则输出 NO。表达式长度小于 255，左圆括号少于 20 个。
输入格式
一行：表达式。
输出格式
一行：YES 或 NO。

输入 2*(x+y)/(1-x)@
输出 YES

输入 (25+x)*(a*(a+b+b)@
输出 NO
"""
other = []
bracket = []

found = False
lamba = list(map(str,input().strip()))

for i in range(len(lamba)):
    if lamba[i] == '(':
        bracket.append(lamba[i])
    elif lamba[i] == ')':
        if len(bracket) > 0:
            bracket.pop()
        else:
            found =True
            print("NO")
            break


if not found:
    if len(bracket) == 0:
        print("YES")
    else:
        print("NO")

