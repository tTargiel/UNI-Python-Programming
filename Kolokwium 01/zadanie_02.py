from itertools import permutations

tekst = input("Podaj ciąg znaków: ")

cyfry = list(filter(lambda znak: znak.isdigit(), tekst))

if len(cyfry) != 0:
    print(list(permutations(cyfry)))
else:
    print("W podanym ciągu znaków nie znajdują sie cyfry")
