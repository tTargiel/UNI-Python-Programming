def ciag():
    n = int(input("Sumę ilu wyrazów szeregu harmonicznego chcesz policzyć? "))
    suma = 0

    for i in range(n):
        suma += 1 / (i + 1)
    print("Suma", n, "wyrazów =", suma)


ciag()
