import xml.etree.ElementTree as ET


class Kursy:
    def __init__(self, path):
        mytree = ET.parse(path)
        myroot = mytree.getroot()
        self.nazwaWaluty = ["polski zloty"]
        self.przelicznik = [1]
        self.kodWaluty = ["PLN"]
        self.kursSredni = ["1,000"]
        for x in myroot:
            if x.tag == "pozycja":
                self.nazwaWaluty.append(x[0].text)
                self.przelicznik.append(x[1].text)
                self.kodWaluty.append(x[2].text)
                self.kursSredni.append(x[3].text)

    def listaKursow(self):
        for x in range(0, len(self.nazwaWaluty)):
            print(self.nazwaWaluty[x] + " - " + self.kodWaluty[x])

    def fromPLN(self):
        opcja = int(input("Konwersja PLN -> waluta obca - 1,\nKonwersja waluta obca -> PLN - 2: "))
        if opcja == 1:
            doKonwersji = str.upper(input("Wpisz kod waluty na którą chcesz przekonwertować: "))
            indeks = self.kodWaluty.index(doKonwersji)
            wynik = (float(input("Ile PLN chcesz przekonwertować? ")) / float(self.kursSredni[indeks].replace(",", ".")) * int(self.przelicznik[indeks]))
            print("{0} {1}".format(round(wynik, 2), doKonwersji))
        elif opcja == 2:
            doKonwersji = str.upper(input("Wpisz kod waluty z której chcesz przekonwertować na PLN: "))
            indeks = self.kodWaluty.index(doKonwersji)
            wynik = (float(input("Ile " + doKonwersji + " chcesz przekonwertować? ")) * float(self.kursSredni[indeks].replace(",", "."))) / int(self.przelicznik[indeks])
            print("{0} {1}".format(round(wynik, 2), "PLN"))

    def DiffToDiff(self):
        doKonwersji = str.upper(input("Wpisz kod waluty z której chcesz przekonwertować: "))
        indeksDK = self.kodWaluty.index(doKonwersji)
        konwertujDo = str.upper(input("Wpisz kod waluty na którą chcesz przekonwertować: "))
        indeksKD = self.kodWaluty.index(konwertujDo)
        half = (float(input("Ile " + doKonwersji + " chcesz przekonwertować? ")) * float(self.kursSredni[indeksDK].replace(",", ".")) ) / int(self.przelicznik[indeksDK])
        wynik = (half / float(self.kursSredni[indeksKD].replace(",", ".")) * int(self.przelicznik[indeksKD]))
        print("{0} {1}".format(round(wynik, 2), konwertujDo))


kursy = Kursy("kursy.xml")
option = int(input("Lista dostępnych walut - 1, Konwersja PLN <-> waluta obca - 2, Waluta obca <-> Inna waluta obca - 3: "))

if option == 1:
    kursy.listaKursow()
elif option == 2:
    kursy.fromPLN()
elif option == 3:
    kursy.DiffToDiff()
