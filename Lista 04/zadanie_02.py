lista = [1, 1, 1, 2]
print(lista)


def usunDuplikaty(lista):
    listaNowa = []
    for i in lista:
        if i in listaNowa:
            listaNowa = listaNowa
        else:
            listaNowa.append(i)
    print(listaNowa)


usunDuplikaty(lista)
