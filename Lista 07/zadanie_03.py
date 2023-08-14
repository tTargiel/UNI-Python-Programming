import random
import time


def bubbleSort(n):
    tab = []
    for i in range(n):
        tab.append(random.randint(1, 20))
    print("Nieposortowana tablica:\n", tab, "\n")
    i = 0
    print("Kolejne kroki sortowania bąbelkowego:")
    while i < len(tab) - 1:
        start = time.process_time()
        j = 0
        while j < len(tab) - 1 - i:
            if tab[j] > tab[j + 1]:
                tab[j], tab[j + 1] = tab[j + 1], tab[j]
            j += 1
        i += 1
        print(tab)
    print("\nPosortowana tablica:\n", tab, "\n\nCzas sortowania:", time.process_time() - start)
    return ""


print(bubbleSort(50))
