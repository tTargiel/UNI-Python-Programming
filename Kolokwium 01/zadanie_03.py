import math

try:
    x1 = float(input("Podaj miejsce punktu x1: "))
except ValueError:
    print("Podana wartość nie jest liczbą")

try:
    y1 = float(input("Podaj miejsce punktu y1: "))
except ValueError:
    print("Podana wartość nie jest liczbą")

try:
    x2 = float(input("Podaj miejsce punktu x2: "))
except ValueError:
    print("Podana wartość nie jest liczbą")

try:
    y2 = float(input("Podaj miejsce punktu y2: "))
except ValueError:
    print("Podana wartość nie jest liczbą")

jednostka = input("Podaj jednostkę: ")

d = math.sqrt(((x2 - x2) ** 2) + (y2 - y1) ** 2)
print("Odległość między punktami wynosi: ", d, jednostka)
