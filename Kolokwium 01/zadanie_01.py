lista = [2, (17, -8), 6, "Ala", "Python", -4.0, "Ela"]

wynik1 = max(filter(lambda s: isinstance(s, str), lista))
wynik2 = min(filter(lambda var: isinstance(var, (int, float, complex)), lista))

print("Najdłuższy ciąg znaków w liście to: " + wynik1)
print("Najmniejsza liczba w liście to: " + str(wynik2))
