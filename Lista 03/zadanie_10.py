lista = []

i = 100

while i <= 400:
    string = str(i)
    x = 0
    for j in range(3):
        if int(string[j]) % 2 == 0:
            x = x + 1
    if x == len(string):
        lista.append(string)
    i = i + 1

print(lista)
