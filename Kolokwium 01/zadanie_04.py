import string

tekst = input("Napisz coś: ")

alfabet_string = string.ascii_letters
alfabet_lista = list(alfabet_string)

czestoscLiter = []

for i in alfabet_lista:
    ileLiter = tekst.count(i)
    if ileLiter != 0:
        danaLitera = i + ":" + str(ileLiter)
        czestoscLiter.append(danaLitera)
print(czestoscLiter, "Ilość liter: ", len(tekst))
