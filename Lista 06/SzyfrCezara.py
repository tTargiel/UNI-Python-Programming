def szyfruj(zdanie, przesuniecie):
    zaszyfrowane = ""
    for i in zdanie:
        j = ord(i)
        if (j > 64 and j < 91) or (j > 96 and j < 123):
            if i.isupper():
                zaszyfrowane += chr((j + przesuniecie - 65) % 26 + 65)
            else:
                zaszyfrowane += chr((j + przesuniecie - 97) % 26 + 97)
        else:
            zaszyfrowane += i
    return zaszyfrowane


def deszyfruj(szyfr, przesuniecie):
    odszyfrowane = ""
    for i in szyfr:
        j = ord(i)
        if (j > 64 and j < 91) or (j > 96 and j < 123):
            if i.isupper():
                odszyfrowane += chr((j - przesuniecie - 65) % 26 + 65)
            else:
                odszyfrowane += chr((j - przesuniecie - 97) % 26 + 97)
        else:
            odszyfrowane += i
    return odszyfrowane
