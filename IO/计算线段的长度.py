Xa, Ya = map(int, input().split())
Xb, Yb = map(int, input().split())

if Ya >= Yb and Xa >= Xb:
    length = (((Ya - Yb) ** 2) + ((Xa - Xb) ** 2)) ** (1 / 2)
elif Ya <= Yb and Xa >= Xb:
    length = (((Yb - Ya) ** 2) + ((Xa - Xb) ** 2)) ** (1 / 2)
elif Ya >= Yb and Xa <= Xb:
    length = ((Ya - Yb) ** 2 + (Xb - Xa) ** 2) * (1 / 2)
else:
    length = ((Yb - Ya) ** 2 + (Xb - Xa) ** 2) * (1 / 2)

print(f"{length:.3f}")