import os


def checkPesel():
    odczyt = []
    dane = []
    pesel = str
    deszyfrFile = open("PESEL_INFO.txt", "w+")
    
    if os.path.isfile("PESEL.txt"):  # Jeśli uda się otworzyć
        with open("PESEL.txt", "r") as file:
            odczyt = file.readlines()  # Odczytuje każdą linijkę pliku
            
            for i in range(len(odczyt)):
                pesel = odczyt[i]
                pesel = pesel.replace("\n", "")  # Usuwamy znaki końca linii
                
                if (len(pesel) == 11):  # Sprawdza czy pesel ma odpowiednią liczbę znaków
                    dane.append(pesel)

            for i in range(len(dane)):
                pesel = dane[i]
                gender = str
                year = int(pesel[0:2])
                month = int(pesel[2:4])
                day = int(pesel[4:6])
                
                if month - 20 >= 1:
                    year += 2000
                else:
                    year += 1900
                
                if (pesel[9]) in "02468":  # Jeżeli na pozycji 9 jest liczba parzysta, to płeć = kobieta
                    gender = "K"
                else:
                    gender = "M"
                
                deszyfrFile.write(
                    pesel
                    + ":\ndata urodzenia: {0}-{1}-{2};".format(year, month, day)
                    + "\tpłeć: {0}".format(gender)
                    + "\n\n"
                )


checkPesel()
