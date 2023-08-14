lista = ["Kasia", "Basia", "Marek", "Darek"]
print(lista)
lista.append("Józek")
print(lista)
lista2 = ["Ania", "Basia"]
lista.extend(lista2)
print(lista)
lista.sort()
print(lista)
print(lista[3])
print(lista[:2])
print(lista[-2:])
ileBasiMiNiePasi = lista.count("Basia")
for i in range(ileBasiMiNiePasi):
    lista.remove("Basia")
print(lista)
print(len(lista))
krotka = tuple(lista)
print("Utworzono krotkę: ", krotka)
