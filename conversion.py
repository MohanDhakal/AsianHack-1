import requests
import json
from requests.exceptions import ConnectionError

with open('rates.json') as f:
    rates_offline = json.load(f)

YOUR_APP_ID = "b05b1cdcf60a438c891c4cf9e12db721"

class CurrencyConverter:
    def __init__(self, YOUR_APP_ID, symbols):
            self.YOUR_APP_ID = YOUR_APP_ID
            self.symbols = symbols
            self._symbols = ",".join([str(s) for s in symbols])

            try:
        
                r = requests.get(
                    "https://openexchangerates.org/api/latest.json",
                    params = {
                        "app_id" : self.YOUR_APP_ID,
                        "symbols" : self._symbols,
                        "show_alternatives": True
                            }
                    )
                self.rates_ = r.json()["rates"]
                self.rates_["USD"] = 1
            except ConnectionError:
                self.rates_ = rates_offline["rates"]
                self.rates_["USD"] = 1

    def convert(self, value, symbol_from, symbol_to):
        try:
            return value * 1/self.rates_.get(symbol_from) * self.rates_.get(symbol_to)
        except TypeError:
            print("Error")
            return None


converter = CurrencyConverter("b05b1cdcf60a438c891c4cf9e12db721", ["USD", "NPR", "INR", "EUR", "JPY"])