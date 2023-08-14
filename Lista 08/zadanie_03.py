import random


def pesel():
    year = random.randint(1900, 2099)  # Losuje rok urodzenia - liczbę z przedziału 1900 - 2099
    rr = str(year)
    rr = rr[2:]  # Wycina dwa ostatnie znaki roku - będą początkiem numeru PESEL

    if (year < 2000):  # Generuje kod miesiąca ze względu na stulecie, kolejne 2 znaki do numeru
        month = random.randint(1, 12)
    else:
        month = random.randint(1, 12) + 20

    if month % 2 == 0:  # Generuje dzień ze względu na miesiąc
        day = random.randint(1, 30)
    elif month % 2 == 1:
        day = random.randint(1, 31)
    elif month == 2 or month == 22:  # Dla lutego
        if year % 4 == 0:  # Jeśli rok przestępny
            day = random.randint(1, 29)
        else:
            day = random.randint(1, 28)

    pppp = ""
    for i in range(4):
        p = random.randint(0, 9)
        pppp += str(p)

    if month < 10:
        month = "0" + str(month)
    
    if day < 10:
        day = "0" + str(day)
    
    pesel = str(rr) + str(month) + str(day) + str(pppp)
    k_factors = [1, 3, 7, 9, 1, 3, 7, 9, 1, 3]
    k = int(0)
    
    for i in range(10):
        factor = int(pesel[i]) * int(k_factors[i])
        x = str(factor)
        x = x[-1]
        k += int(x)
    
    z = str(k)
    z = z[-1]
    k = 10 - int(z)
    pesel += str(k)
    
    return pesel


file = open("PESEL.txt", "w+")

for i in range(10):
    file.write(pesel() + "\n")
