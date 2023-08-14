def obwod(a, b, c):
    obw = a + b + c
    return obw


def pole(a, b, c):
    p = (a + b + c) / 2
    pole = (p * (p - a) * (p - b) * (p - c)) ** (1 / 2)  # Wzór Herona
    return pole


def jakiTyp(a, b, c):
    if a == b == c:
        typ = "równoboczny"
    elif (a == b != c) or (a == c != b) or (b == c != a):
        typ = "równoramienny"
    elif a != b != c:
        typ = "różnoboczny"
    return typ


def jakiKat(a, b, c):
    if (
        (a ** 2 + b ** 2 == c ** 2)
        or (a ** 2 + c ** 2 == b ** 2)
        or (b ** 2 + c ** 2 == a ** 2)
    ):
        kat = "prostokątny"
    elif (
        (a ** 2 + b ** 2 > c ** 2)
        or (a ** 2 + c ** 2 > b ** 2)
        or (b ** 2 + c ** 2 > a ** 2)
    ):
        kat = "ostrokątny"
    else:
        kat = "rozwartokątny"
    return kat
