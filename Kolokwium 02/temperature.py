import random


def temperature_converter(T: float, Cel2Far: bool) -> float:
    if Cel2Far == 1:
        T = float(T)
        temperature = (T * 1.8) + 32
    elif Cel2Far == 0:
        temperature = (T - 32) / 1.8
    else:
        print("Podano nieprawidłowe argumenty")
    return temperature


def generate_temperature(N: int):
    generatedTemp = ""
    for i in range(0, N):
        generatedTemp += str(round(random.uniform(-273.15, 100.0), 2)) + "\n"
    return generatedTemp
