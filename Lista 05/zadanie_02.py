def function(liczba):
    lista = []

    jednosci = [
        "",
        "jeden",
        "dwa",
        "trzy",
        "cztery",
        "pięć",
        "sześć",
        "siedem",
        "osiem",
        "dziewięć",
        "dziesięć",
        "jedenaście",
        "dwanaście",
        "trzynaście",
        "czternaście",
        "pietnaście",
        "szesnaście",
        "siedemnaście",
        "osiemnaście",
        "dziewiętnaście",
    ]

    dziesiatki = [
        "",
        "",
        "dwadzieścia ",
        "trzydzieści ",
        "czterdzieści ",
        "pięćdziesiąt ",
        "sześćdziesiąt ",
        "siedemdziesiąt ",
        "osiemdziesiąt ",
        "dziewięćdziesiąt ",
    ]

    setki = [
        "",
        "sto ",
        "dwieście ",
        "trzysta ",
        "czterysta ",
        "pięćset ",
        "sześćset ",
        "siedemset ",
        "osiemset ",
        "dziewięćset ",
    ]

    tysiace = ["", "tysiąc "]

    for i in str(liczba):
        lista.append(int(i))
    for i in range(4 - len(liczba)):
        lista.insert(i, 0)
    return (
        tysiace[lista[0]] + setki[lista[1]] + dziesiatki[lista[2]] + jednosci[lista[3]]
    )


print(function(input("Wpisz liczbę znajdującą się w zakresie od 1 do 1999: ")))
