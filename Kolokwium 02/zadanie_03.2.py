import temperature as temp

try:
    tempPlik = open("temperatura.txt", "r").readlines()
    try:
        tempFPlik = open("temperatura_F.txt", "w")
        for linijka in tempPlik:
            tempFPlik.write(str(round(temp.temperature_converter(linijka, 1), 2)) + "\n")
        tempFPlik.close()
    except OSError:
        print("Wystąpił błąd podczas tworzenia pliku")
except OSError:
    print("Wystąpił błąd podczas odczytywania pliku")
