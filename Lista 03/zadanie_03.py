print("Podaj wartości parametów funkcji kwadratowej")
a = int(input("Podaj wartość parametru a (pamiętaj że musi być inna od 0!): "))
while a == 0:
    print("Wprowadziłeś złą wartość!")
    a = int(input("Podaj wartość parametru a (pamiętaj że musi być inna od 0!): "))
    if a != 0:
        break

b = int(input("Podaj wartość parametru b: "))
c = int(input("Podaj wartość parametru c: "))

delta = b ** 2 - 4 * a * c

if delta > 0:
    x1 = (-b + (delta) ** (1 / 2)) / (2 * a)
    x2 = (-b - (delta) ** (1 / 2)) / (2 * a)
    print("x1 =", x1, "x2 =", x2)
elif delta == 0:
    print("delta = 0, twoja funkcja ma tylko jedno rozwiązanie")
    x = (-b) / (2 * a)
    print("x", x)
else:
    print("Brak rozwiązań")
