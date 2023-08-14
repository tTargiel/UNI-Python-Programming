import random
import time


def insertSort(n):
    tab = []
    for i in range(n):
        tab.append(random.randint(1, 20))
    print("Nieposortowana tablica:\n", tab, "\n")
    i = 1
    while i < len(tab):
        start = time.process_time()
        key = tab[i]
        j = i - 1
        while j >= 0 and key < tab[j]:
            tab[j + 1] = tab[j]
            j -= 1
        tab[j + 1] = key
        i += 1
    print("Posortowana tablica:\n", tab, "\n\nCzas sortowania:", time.process_time() - start)
    return ""


print(insertSort(50))
