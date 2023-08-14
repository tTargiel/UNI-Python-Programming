kluczSzyfrujacy = {"a": "y", "e": "i", "i": "o", "o": "a", "y": "e"}
kluczDeszyfrujacy = {"y": "a", "i": "e", "o": "i", "a": "o", "e": "y"}
x = input("Podaj zdanie/słowo: ")
a = int(input("Czy wprowadzony tekst chcesz 0 - zaszyfrować czy 1 - odszyfrować: "))


def szyfruj(x, kluczSzyfrujacy):
    for litera in x:
        if litera in kluczSzyfrujacy.keys():
            x = x.replace(litera, kluczSzyfrujacy[litera])
    return x


def deszyfruj(x, kluczDeszyfrujacy):
    for litera in x:
        if litera in kluczDeszyfrujacy.keys():
            x = x.replace(litera, kluczDeszyfrujacy[litera])
    return x


if a == 0:
    print(szyfruj(x, kluczSzyfrujacy))
elif a == 1:
    print(deszyfruj(x, kluczDeszyfrujacy))
else:
    print("Taka opcja nie istnieje!")
