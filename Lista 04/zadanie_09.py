def program():
    n = int(input("Silnię jakiej liczby chcesz obliczyć? "))

    silnia = 1
    j = 1

    for i in range(n):
        silnia *= j
        j += 1

    print(f"{n}! =", silnia)


program()
