class CiagArtmetyczny:
    def __init__(self, a1, r, n=1):
        """Inicjuje ciąg arytmetyczny"""

        self.__a1 = a1
        self.__r = r
        self.__wyrazy = [a1]

        if n > 1:
            for _ in range(n - 1):
                self.__wyrazy.append(self.__wyrazy[-1] + self.__r)

    def __iter__(self):
        """Umożliwia iterację po ciągu"""

        for a in self.__wyrazy:
            yield a

    def __str__(self):
        """Zwraca wyrazy ciągu wraz z jego parametrami"""

        s = "Ciąg arytmetyczny ({a1}, {r}, {len}):".format(a1=self.__a1, r=self.__r, len=self.__len__())

        for wyraz in self:
            s += " " + str(wyraz)

        return s

    def __len__(self):
        """Zwraca ilość wyrazów ciągu"""

        return len(self.__wyrazy)

    def __next__(self):
        """Generuje kolejny wyraz ciągu"""

        self.__wyrazy.append(self.__wyrazy[-1] + self.__r)

    def zapisz(self, nazwaPliku):
        """Zapisuje ciąg do pliku"""

        with open(nazwaPliku, "w") as plik:
            plik.write(self.__str__())


ciag = CiagArtmetyczny(2, 2, 8)

print(ciag)
print(len(ciag), "\n")

next(ciag)
print(ciag)
print(len(ciag))

ciag.zapisz("ciag.txt")
