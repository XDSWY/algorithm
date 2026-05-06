x = float(input())
result = 0

if 0 <= x < 5:
    result = -x + 2.5
    print(f"{result:.3f}")
elif 5 <= x < 10:
    result = 2 - 1.5 * (x - 3) * (x - 3)
    print(f"{result:.3f}")
elif 10 <= x < 20:
    result = (x / 2) - 1.5
    print(f"{result:.3f}")
