import math

r = float(input())

p = r * 2
d = math.floor((math.pi * p) * 10000) / 10000
s = math.floor(math.pi * (r ** 2) * 10000) / 10000

print(f"{p:.4f} {d:.4f} {s:.4f}")