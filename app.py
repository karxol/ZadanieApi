import requests
from flask import Flask , render_template , request



response = requests.get("http://api.nbp.pl/api/exchangerates/tables/C?format=json")
data = response.json()

rates = data[0]["rates"]
codes = [currency["code"] for currency in rates]

data_kursu = data[0]["tradingDate"]

app = Flask(__name__)


@app.route("/" , methods=["GET", "POST"])
def kantor():
    kwota = None
    if request.method == "POST":
        amount = request.form["amount"]

        for rate in rates:
            if rate["code"] == request.form["codes"]:
                try:
                    kwota = round((float(rate["ask"]) * float(amount)), 2)
                except ValueError:
                    pass
    
    return render_template("base.html", codes=codes, kwota=kwota, data_kursu=data_kursu)