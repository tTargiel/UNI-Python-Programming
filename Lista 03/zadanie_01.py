a = input("Podaj literę: ").lower()

samogloski = ("a", "ą", "e", "ę", "i", "o", "ó", "u", "y")
spolgloski = ("b", "c", "ć", "cz", "d", "f", "g", "h", "ch", "j", "k", "l", "ł", "m", "n", "ń", "p", "q", "r", "s", "ś", "sz", "t", "w", "z", "ź", "ż")

if a in samogloski:
    print("Ta litera jest samogłoską")

elif a in spolgloski:
    print("Ta litera jest spółgłoską")

else:
    print("Nie podano litery")
