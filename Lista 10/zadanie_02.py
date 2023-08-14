from itertools import combinations


class Podlisty:
    def __init__(self, lista):
        self.lista = lista

    def comb(self):
        for n in range(len(self.lista) + 1):
            comb = combinations(self.lista, n)
            for i in list(comb):
                print(i)


ToCombine = Podlisty([1, 2, 3])
ToCombine.comb()
