m = int(input("Wprowadź liczbę wierszy: "))
n = int(input("Wprowadź liczbę kolumn: "))

tab = []
for i in range(m):
    tab.append([])
    for j in range(n):
        tab[i].append(i * j)

print(tab)
