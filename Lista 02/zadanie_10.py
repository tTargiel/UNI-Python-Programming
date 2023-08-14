lista = []
for i in range(3, 100, 3):
    lista.append(i)
print(lista)
del lista[4::3]
print(lista)
print(sum(lista) / len(lista))
