def trojkatPascala():
    n = int(input("Ile wierszy trójkąta Pascala mam wypisać? "))

    A = [[0 for i in range(n)] for j in range(n)]
    for i in range(0, n):
        for j in range(0, i + 1):
            if i == j or j == 0:
                A[i][j] = 1
            else:
                A[i][j] = A[i - 1][j - 1] + A[i - 1][j]
            print(A[i][j], end=" ")
        print()


trojkatPascala()
