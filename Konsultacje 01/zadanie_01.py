import math


def wielomian(x, a):
    w = 0
    for i in a:
        if int(i) == 1:
            w += int(i)
        else:
            iks = math.pow(x, int(i))
            w += int(i) * iks
    return w


x = int(input("Wpisz x: "))

a_string = input("Wpisz dowolne N wyrazów wielomianu (zachowując między każdym wyrazem spację): ")
while not a_string:
    a_string = input("Wpisz dowolne N wyrazów wielomianu (zachowując między każdym wyrazem spację): ")

a = a_string.split()
print(wielomian(x, a))
