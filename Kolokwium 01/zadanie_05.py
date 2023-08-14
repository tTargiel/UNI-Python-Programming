try:
    x = int(input("Podaj liczbę całkowitą: "))
    run = 1
except ValueError:
    print("Wprowadzono niepoprawne dane")
    run = 0

while run == 1:
    if x < 0:
        print("Liczba nie może być ujemna")
    if x > 0:
        while x > 1:
            if x % 2 == 0:
                x /= 2
                print(x)
            elif x % 2 == 1:
                x = 3 * x + 1
                print(x)
            elif x == 1:
                break
    run = 0
