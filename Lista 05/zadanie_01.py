liczba = str(input("Wpisz liczbę: ").lower())


def function(liczba):
    tab = []
    numer = 0
    if "jeden" in liczba:
        tab.append(1)
    elif "dwa" in liczba:
        tab.append(2)
    elif "trzy" in liczba:
        tab.append(3)
    elif "cztery" in liczba:
        tab.append(4)
    elif "pięć" in liczba:
        tab.append(5)
    elif "sześć" in liczba:
        tab.append(6)
    elif "siedem" in liczba:
        tab.append(7)
    elif "osiem" in liczba:
        tab.append(8)
    elif "dziewięć" in liczba:
        tab.append(9)
    if "dziesięć" in liczba:
        tab.append(10)
    if "jedenaście" in liczba:
        tab.append(11)
    if "dwanaście" in liczba:
        tab.append(12)
    if "trzynaście" in liczba:
        tab.append(13)
    if "czternaście" in liczba:
        tab.append(14)
    if "piętnaście" in liczba:
        tab.append(15)
    if "szesnaście" in liczba:
        tab.append(16)
    if "siedemnaście" in liczba:
        tab.append(17)
    if "osiemnaście" in liczba:
        tab.append(18)
    if "dziewiętnaście" in liczba:
        tab.append(19)
    if "dwadzieścia" in liczba:
        tab.append(20)
    if "trzydzieści" in liczba:
        tab.append(30)
    if "czterdzieści" in liczba:
        tab.append(40)
    if "pięćdziesiąt" in liczba:
        tab.append(50)
    for i in range(len(tab)):
        numer += tab[i]
    return numer


print(function(liczba))
