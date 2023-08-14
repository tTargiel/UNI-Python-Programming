def ciag():
    n = int(input("Który wyraz ciągu chcesz obliczyć? "))
    x = int(
        input(
            "Czy chcesz zmienić wartość pierwszego wyrazu ciągu z domyślnej (a1=1) na inną? (0 - nie, 1 - tak): "
        )
    )

    if x == 1:
        a1 = int(input("Podaj wartość dla a1: "))
    else:
        a1 = 1

    y = int(
        input(
            "Czy chcesz zmienić wartość dla iloczynu ciągu z domyślnej (q=2) na inną? (0 - nie, 1 - tak): "
        )
    )

    if y == 1:
        q = int(input("Podaj wartość dla q: "))
    else:
        q = 2

    print(n, "wyraz tego ciągu to: ", a1 * q ** (n - 1))


ciag()
