import math

print("Wpisz 0 - jeżeli chcesz przekonwertować radiany na stopnie, lub 1 - by dokonać konwersji odwrotnej")
a = int(input())


def konwertuj(a):
    if a == 0:
        x = float(input("Podaj radiany: "))
        print(x * (180 / math.pi), "°")
    elif a == 1:
        x = float(input("Podaj stopnie: "))
        print(x * (math.pi / 180), "rad")
    else:
        print("Podana przez ciebie wartość nie odpowiada żadnej operacji!")


konwertuj(a)
