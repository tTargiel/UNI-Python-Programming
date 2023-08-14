import math


class Fraction:
    def __init__(self, a, b):
        self.a = int(a)
        self.b = int(b)

    def __str__(self):
        return f"{self.a}/{self.b}"

    def skroc(self):
        nwd = math.gcd(self.a, self.b)
        self.a //= nwd
        self.b //= nwd
        return f"{self.a}/{self.b}"

    def __add__(self, other):
        lewy_licznik = self.a * other.b
        prawy_licznik = other.a * self.b
        wynik = Fraction(lewy_licznik + prawy_licznik, self.b * other.b)
        wynik.skroc()
        return wynik

    def __sub__(self, other):
        lewy_licznik = self.a * other.b
        prawy_licznik = other.a * self.b
        wynik = Fraction(lewy_licznik - prawy_licznik, self.b * other.b)
        wynik.skroc()
        return wynik

    def __mul__(self, other):
        wynik = Fraction(self.a * other.a, self.b * other.b)
        wynik.skroc()
        return wynik

    def __truediv__(self, other):
        wynik = Fraction(self.a * other.b, self.b * other.a)
        wynik.skroc()
        return wynik


a = Fraction(4, 2)
b = Fraction(1, 3)

print(a)
a.skroc()
print(a)

c = a * a + b

d = b - b / a

print(c)
print(d)
