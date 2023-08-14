from itertools import permutations


def permutacje():
    a = input(
        "Wprowadź wszystkie elementy z których program ma stworzyć permutacje. Nie rób spacji ani nie stawiaj przecinków!\n"
    )
    b = permutations(a)

    for i in b:
        print(i)


permutacje()
