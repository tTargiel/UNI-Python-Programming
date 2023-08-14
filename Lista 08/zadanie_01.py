import SzyfrCezara as SC
import os
from datetime import datetime

print("Current working directory:", os.getcwd())
path = str(input("Podaj ścieżkę do pliku:\n"))
shift = int(input("Wprowadź przesunięcie, którego chcesz użyć (1-10):\n"))

x = datetime.now()

if shift <= 10 or shift >= 1:
    try:
        baseFile = open(path, "r").read()  # Otwiera plik z podanej ścieżki w trybie read i go odczytuje
        encrypted = open("plik_zaszyfrowany_{0}_{1}.{2}.{3}.txt".format(shift, x.day, x.month, x.year), "w")  # Otwiera plik w trybie write
        encrypted.write(SC.szyfruj(baseFile, shift))  # Zapisuje do pliku zaszyfrowane dane z pierwszego pliku
    except OSError:
        print("Wystąpił błąd podczas tworzenia pliku")
else:
    print("Podano złe przesunięcie (dobre znajduje się w zakresie 1-10)")
