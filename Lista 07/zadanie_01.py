import time

n = int(input("Ile wyrazów ciągu fibonacciego mam wypisać? "))


def fib_iteracyjnie(n):
    a = 0
    b = 1
    if n <= 0:
        print("Podano nieprawidłową ilość wyrazów do wyznaczenia")
    else:
        for i in range(0, n):
            if i == 0:
                print(a)
            elif i == 1:
                print(b)
            else:
                c = a + b
                a = b
                b = c
                print(c)
    return ""


def fib_rekurencyjnie(n):
    if n < 0:
        print("Podano nieprawidłową ilość wyrazów do wyznaczenia")
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fib_rekurencyjnie(n - 1) + fib_rekurencyjnie(n - 2)


print("Iteracyjnie:")
iteracjaStart = time.process_time()
print(fib_iteracyjnie(n))
print("Czas dla funkcji iteracyjnej:", time.process_time() - iteracjaStart, "s\n\n")


print("Rekurencyjnie:")
rekurencjaStart = time.process_time()
for x in range(n):
    print(fib_rekurencyjnie(x + 1))
print("\nCzas dla funkcji rekurencyjnej:", time.process_time() - rekurencjaStart, "s")
