import sys
import urllib.request
import urllib.parse

arg1Lista = sys.argv[1:]

for urlElementListy in arg1Lista:
    url = ""
    url += urlElementListy

nazwaPliku = ""

try:
    if url[-1] == "/":
        nazwaPliku = "index.html"
    else:
        for i in range(1, len(url)):
            if url[-i] == "/":
                nazwaPliku = url[-i + 1 : len(url)] + ".html"
                break
except:
    print("Nie podano adresu URL")

try:
    html = urllib.request.urlopen(url)
    with open(nazwaPliku, "w") as sys.stdout:
        print(html.read())

except Exception as e:
    print("Napotkano błąd:", e)
