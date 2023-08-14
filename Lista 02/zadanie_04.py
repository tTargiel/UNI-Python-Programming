napis = input("Podaj napis: ")
temp = napis[1:]
print(napis[:1] + temp.replace(napis[:1], "$"))
