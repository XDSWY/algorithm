"""
物品应根据其价格和她的喜好来选择。西瓜是第一选择，石榴是第二选择，坚果是第三选择。如果 Mahya 的预算不足以购买任何物品，她将完全放弃购买。

输入格式
输入包含以下内容：
第一行包含一个整数 b (0≤b≤10的6次方)，表示 Mahya 的预算，单位为里亚尔。
接下来的三行分别包含西瓜、石榴和坚果的价格，每个价格均为不超过10的6次方的非负整数。

输出格式
输出 Mahya 根据其偏好列表能够负担得起的第一个物品的名称："Watermelon"、"Pomegranates" 或 "Nuts"。
如果她的预算不足以购买任何物品，则输出 "Nothing"。


输入
150
200
95
130

输出
Pomegranates
"""

b = int(input())
watermelon = int(input())
pomegranates = int(input())
nuts = int(input())

if b > watermelon:
    print("Watermelon")
elif pomegranates < b < watermelon:
    print("Pomegranates")
elif nuts < b < pomegranates and b < watermelon:
    print("Nuts")
else:
    print("Nothing")