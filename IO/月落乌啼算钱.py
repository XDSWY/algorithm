n = int(input())
from math import sqrt

fn = ((((1+sqrt(5))/2)**n) - (((1-sqrt(5))/2)**n)) /sqrt(5)

print(f"{fn:.2f}")
