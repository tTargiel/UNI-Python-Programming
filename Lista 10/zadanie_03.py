from itertools import combinations
import random


class Podlisty:
    def __init__(self, N):
        self.N = N

    def triple(self):
        lista = []
        for i in range(self.N):
            lista.append(random.randint(-10, 10))
        comb = combinations(lista, 3)
        for i in list(comb):
            if sum(i) == 0:
                print(i)


array = Podlisty(10)
array.triple()
