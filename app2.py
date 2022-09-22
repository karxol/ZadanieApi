import requests
from flask import Flask , render_template , request



response = requests.get("http://api.nbp.pl/api/exchangerates/tables/C?format=json")
data = response.json()

with open("rates.csv", "w") as plik:
        
    for rate in data[0]["rates"]:
        plik.write(rate.get("currency"))
        plik.write(";")
        plik.write(rate.get("code"))
        plik.write(";")
        plik.write(str(rate.get("bid")))
        plik.write(";")
        plik.write(str(rate.get("ask")))
        plik.write("\n")