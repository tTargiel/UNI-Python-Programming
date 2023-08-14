import sys

try:
    n = int(sys.argv[1:][0])
    for i in range(0, n):
        for j in range(0, n):
            print(i * j, end=" ")
        print("\n")
except:
    print("Nie podano argumentu lub jest on niepoprawny")
