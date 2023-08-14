print(
    "Podaj dwie liczby całkowite, program ten następnie wyliczy ich największy wspólny dzielnik: "
)
a = int(input())
b = int(input())

czynnikiA = []
czynnikiB = []
ilo = []
nwd = 1


def rozlozA(a):
    x = 2
    while a != 1:
        while a % x == 0:
            a //= x
            czynnikiA.append(x)
        x += 1
    return czynnikiA


def rozlozB(b):
    x = 2
    while b != 1:
        while b % x == 0:
            b //= x
            czynnikiB.append(x)
        x += 1
    return czynnikiB


rozlozA(a)
rozlozB(b)

for i in czynnikiA:

    if i in czynnikiB:
        ilo.append(i)
        czynnikiB.index(i)
        czynnikiB.remove(i)

for i in ilo:
    nwd *= i

print("NWD =", nwd)
