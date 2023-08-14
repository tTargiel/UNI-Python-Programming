import re

tekst = "alcohol clarify cart seasonal Execute offset see cruel background pile beach Survivor damn hilarious strategic wrestle Few negligence rock injury Extension forget commission broadcast characteristic Coverage leg shine training education belt Distributor multimedia fleet motif headline leader revive Journal Momentum even cause fine run poem captain wait retiree Package profile"
slowaAE = re.findall(r"\b[aAeE]\w+", tekst)

print("Znalezione słowa zaczynające się na a lub e:", slowaAE)
