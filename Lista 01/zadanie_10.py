import cmath

x = int(input())
z = complex(x, x)
# print(z)
print(cmath.sin(z))
a = cmath.sin(z)
print(cmath.cos(z))
b = cmath.cos(z)
print(a ** 2 + b ** 2)
if a ** 2 + b ** 2 == 1:
    print("Zależność jedynki trygonometrycznej dla liczby zespolonej jest spełniona")
else:
    print("Zależność jedynki trygonometrycznej dla liczby zespolonej nie jest spełniona")
