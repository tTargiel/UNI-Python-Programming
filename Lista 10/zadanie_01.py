import math


class Kolo:
    def __init__(self, r):
        self.r = r

    def Pole(self):
        print(math.pi * self.r ** 2)

    def Obwod(self):
        print(2 * math.pi * self.r)


licz = Kolo(8)
licz.Pole()
licz.Obwod()
