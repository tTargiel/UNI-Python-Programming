import re

print("Za chwilę podasz swoje nowe hasło, pamiętaj że musi zawierać dużą i mała literę, cyfrę oraz znak specjalny. Nie może być krótsze niż 6 znaków ani dłuższe niż 16.")
haslo = str(input("Wprowadź swoje nowe hasło: "))

petla = True

while petla:
    if not re.search("[a-z]", haslo):
        break

    elif not re.search("[A-Z]", haslo):
        break

    elif not re.search("[0-9]", haslo):
        break

    elif not re.search("[$ , # , @, %, &, *, !]", haslo):
        break

    elif len(haslo) < 6 or len(haslo) > 16:
        break

    else:
        print("Twoje hasło jest prawidłowe")
        petla = False
        break

if petla:
    print("Twoje hasło jest nieprawidłowe")
