from math import atan, pi

R = float(input("Podaj część rzeczywistą liczby zespolonej: "))
I = float(input("Podaj część urojoną liczby zespolonej: "))
z = complex(R, I)
print("Modułem podanej liczby rzeczywistej ", z, " jest: ", abs(z))
if R > 0:
    phi = atan(I / R)
elif R < 0:
    phi = atan(I / R) + pi
elif R == 0 and I > 0:
    phi = 0
elif R == 0 and I < 0:
    phi = pi
else:
    phi = "NaN"
print("Argumentem podanej liczby rzeczywistej ", z, " jest: ", phi)
print("Sprzężeniem podanej liczby rzeczywistej ", z, " jest: ", z.conjugate())
