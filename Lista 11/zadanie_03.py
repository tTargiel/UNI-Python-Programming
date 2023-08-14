import re

tekst = "blabla dududu kwakwakwa https://www.example.com/balance/amount?ball=bed&birds=adjustment https://border.example.com/ https://example.com/arm/afterthought https://www.example.com/?blood=bells https://www.example.com/boat https://www.example.com/beginner https://www.example.com/ http://www.example.com/bridge.php#behavior https://example.com/ https://example.com/"
adresyUrl = re.findall("http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+", tekst)

print("Znalezione adresy url: ", adresyUrl)
