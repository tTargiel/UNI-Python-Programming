def lookAndSay(n):
    a = "1"  # a to wyraz początkowy
    print(a)
    for i in range(
        1, n
    ):  # Pętla wykona się tyle razy ile wyrazów ciągu kazaliśmy wyliczyć
        ile = 1  # Zmienna ile przechowuje informację o ilości jednakowych znaków (1 to wartość domyślna)
        a += "x"  # Do naszego początkowego/poprzedniego wyrazu dodaje dowolną literę (na potrzeby dalszego działania)
        wyraz = ""  # Zmienna wyraz to n-ty wyraz ciągu
        for j in range(1, len(a)):  # Iteruję tyle razy ile znaków ma nasz wyraz a
            if (
                a[j] != a[j - 1]
            ):  # Jeżeli znak na pozycji j jest różny od znaku na pozycji j - 1 to oznacza, że skończyły się jednakowe znaki i należy do wyrazu końcowego dopisać ile ich było (str(ile)) oraz jakie to znaki były (a[j - 1])
                wyraz += str(ile)  # Ile było jednakowych znaków
                wyraz += a[j - 1]  # Jakie to były znaki
                ile = 1  # Zmienną ile resetuję do wartości domyślnej
            else:
                ile += 1  # Jeżeli znaki na pozycjach j oraz j - 1 były jednakowe, to przekazuję zmiennej ile informację o tym, by zwiększyła się o 1 - występuje kilka jednakowych znaków
        a = wyraz  # Po zakończonym wykonaniu pętli iterowanej po j, otrzymujemy informację o wyrazie n ciągu - jest to jednocześnie wyraz od którego rozpocznie się następna iteracja pętli
        print(a)
    return 1


lookAndSay(int(input("Ile wyrazów ciągu look-and-say mam wyznaczyć? ")))
