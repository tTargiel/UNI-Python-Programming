lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def licz(lista):
    suma = 0
    iloczyn = 1
    for i in range(len(lista)):
        suma += lista[i]
        iloczyn *= lista[i]
    print("Suma = ", suma)
    print("Iloczyn = ", iloczyn)


licz(lista)
