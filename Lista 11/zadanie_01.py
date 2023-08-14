from urllib.request import Request, urlopen
from urllib.error import URLError, HTTPError

req = Request("http://wfa.uni.wroc.pl/pl/tu-nic-nie-ma")

try:
    response = urlopen(req)
except HTTPError as e:
    if e.code == 404:
        print("Błąd HTTP:", e.code, "- Podana strona nie istnieje")
    else:
        print("Serwer nie mógł spełnić twojego żądania")
        print("Błąd HTTP:", e.code)
except URLError as e:
    print("Nie udało się połączyć z serwerem")
    print("Powód:", e.reason)
else:
    print("Podany adres URL jest poprawny oraz dostępny w sieci")
