x = input("Wprowadź liczbę rzymską: ")


def rzymskaDoDziesietnej(x):
    rzymska = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    dziesietna = 0
    for i in range(len(x)):
        if i == 0:
            dziesietna += rzymska[x[i]]
        elif rzymska[x[i]] > rzymska[x[i - 1]]:
            dziesietna += rzymska[x[i]] - 2 * rzymska[x[i - 1]]
        else:
            dziesietna += rzymska[x[i]]
    return dziesietna


print(rzymskaDoDziesietnej(x))
