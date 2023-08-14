n = int(input("Ile wyrazów ciągu fibonacciego mam obliczyć? "))

w1, w2 = 0, 1
x = 0

while x < n:
    print(w1)
    nastepnyWyraz = w1 + w2
    w1 = w2
    w2 = nastepnyWyraz
    x += 1
