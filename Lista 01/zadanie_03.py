from math import sin

a = float(input("Proszę podać długość pierwszego boku: "))
b = float(input("Proszę podać długość drugiego boku: "))
alpha = int(input("Proszę podać miarę kąta między tymi bokami: "))
pole_trojkata = 1 / 2 * a * b * sin(alpha)
print("Pole trójkąta to: ", pole_trojkata)
