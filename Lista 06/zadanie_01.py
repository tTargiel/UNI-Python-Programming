import trojkat

a = float(input("Podaj długość pierwszego boku: "))
b = float(input("Podaj długość drugiego boku: "))
c = float(input("Podaj długość trzeciego boku: "))

if (a < b + c) and (b < a + c) and (c < a + b):
    print("Obwód tego trójkąta wynosi:", trojkat.obwod(a, b, c))
    print("Pole tego trójkąta wynosi:", trojkat.pole(a, b, c))
    print(
        "Ten trójkąt jest:",
        trojkat.jakiTyp(a, b, c),
        "oraz",
        trojkat.jakiKat(a, b, c),
    )
else:
    print("Z takich boków nie da się zbudować trójkąta.")
