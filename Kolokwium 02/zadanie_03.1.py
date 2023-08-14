import temperature as temp
import sys

try:
    n = int(sys.argv[1:][0])
    try:
        tempPlik = open("temperatura.txt", "w")
        tempPlik.write(temp.generate_temperature(n))
        tempPlik.close()
    except OSError:
        print("Wystąpił błąd podczas tworzenia pliku")
except:
    print("Nie podano argumentu lub jest on niepoprawny")
