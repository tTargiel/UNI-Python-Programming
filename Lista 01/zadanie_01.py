a = input()
b = input()
suma = a + b
print(suma)
# Rezultat jest zły ponieważ typ pobieranych danych domyślnie to string, a do działania na liczbach potrzeba... liczb (w naszym przypadku całkowitych)

print("A tak powinno być: ")
a = int(input("Wpisz pierwszą liczbę: "))
b = int(input("Wpisz drugą liczbę: "))
suma = a + b
print(suma)
