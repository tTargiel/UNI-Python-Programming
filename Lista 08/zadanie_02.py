import SzyfrCezara as SC
import os
import re
from datetime import datetime

print("Current working directory:", os.getcwd())
path = str(input("Podaj ścieżkę do zaszyfrowanego pliku:\n"))

try:
    y = re.findall("[0-9]_", path)
    z = y[0]
    shift = int(z[:1])
    x = datetime.now()
    try:
        baseFile = open(path, "r").read()  # Otwiera plik z podanej ścieżki w trybie read i go odczytuje
        encrypted = open("plik_deszyfrowany_{0}_{1}.{2}.{3}.txt".format(shift, x.day, x.month, x.year), "w")  # Otwiera plik w trybie write
        encrypted.write(SC.deszyfruj(baseFile, shift))  # Zapisuje do pliku odszyfrowane dane z pierwszego pliku
    except OSError:
        print("Wystąpił błąd podczas tworzenia pliku")
except:
    print("Podany plik nie posiada instrukcji deszyfrowania")
