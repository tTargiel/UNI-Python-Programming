import numpy
import matplotlib.pyplot as plt

v0 = float(input("Podaj prędkość początkową v0 [m/s]: "))
alpha = float(input("Podaj kąt rzutu a [°]: "))
g = 9.81
v0x = v0 * numpy.cos(numpy.radians(alpha))
v0y = v0 * numpy.sin(numpy.radians(alpha))
tLotu = (2 * v0y) / g
hMax = (v0y * v0y) / 2 * g
zasieg = (2 * v0 ** 2 * (numpy.sin(numpy.radians(alpha))) * (numpy.cos(numpy.radians(alpha)))) / g

print(
    "\nCzas lotu -",
    tLotu,
    "s\nMaksymalna wysokość -",
    hMax,
    "m\nZasięg -",
    zasieg,
    "m",
)

T = list()
Vy = list()
Vx = list()
X = list()
H = list()

for i in numpy.arange(0, tLotu, 0.1):
    T.append(i)
    Vy.append(v0y - g * i)
    Vx.append(v0x)
    X.append(v0x * i)
    H.append((v0y * i - (g * (i ** 2)) / 2))

plt.subplot(3, 1, 1)
plt.plot(T, Vy, label="Vy(t)")
plt.plot(T, Vx, label="Vx(t)")
plt.title("Prędkość chwilowa w kierunku pionowym i poziomym po czasie")
plt.xlabel("t [s]")
plt.ylabel("v [m/s]")
plt.legend()
plt.subplot(3, 1, 2)
plt.plot(X, T)
plt.title("Położenie w funkcji czasu")
plt.xlabel("x [m]")
plt.ylabel("t [s]")
plt.subplot(3, 1, 3)
plt.plot(X, H)
plt.title("Wykres toru rzutu ukośnego")
plt.xlabel("x [m]")
plt.ylabel("h [m]")
plt.show()
