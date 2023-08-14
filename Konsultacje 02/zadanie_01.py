import sys

temp_c = 0.0
temp_f = 0.0

try:
    if sys.argv[2] == "f" or sys.argv[2] == "F":
        temp_f = float(sys.argv[1])
        temp_c = 5 / 9 * (float(sys.argv[1]) - 32)
    elif sys.argv[2] == "c" or sys.argv[2] == "C":
        temp_f = 32 + 9 / 5 * float(sys.argv[1])
        temp_c = float(sys.argv[1])
    else:
        print("Podano błędną jednostkę")
except:
    print("Podano nieprawidłowe argumenty lub nie podano w ogóle")

if len(sys.argv) > 2:
    try:
        file = open(sys.argv[3], "w")
        file.write(f"{temp_c} C\t{temp_f} F")
        file.close()
    except OSError:
        print("Wystąpił błąd podczas tworzenia pliku")
else:
    print(f"{temp_c} C\t{temp_f} F")
