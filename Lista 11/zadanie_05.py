import re

tekst = "PythonPython WordWord pies kot LisLis owca BaranByk"
tekst = re.sub(r"(\w)([A-Z])", r"\1 \2", tekst)

print(tekst)