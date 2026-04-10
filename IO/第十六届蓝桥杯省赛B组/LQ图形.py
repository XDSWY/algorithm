import os
import sys

w, h, v = map(int,input().split())

for i in range(h):
  print("Q" * w)

for i in range(w):
  print("Q" * (w + v))
