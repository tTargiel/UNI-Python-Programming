a = int(input("Podaj pierwszą liczbę: "))
b = int(input("Podaj drugą liczbę (mniejszą niż pierwsza): "))
if b >= a:
    b = int(input("Podaj drugą liczbę (mniejszą niż pierwsza): "))
else:
    Z = b % a
    print(Z)
    Z *= Z + 3
    print(Z)
