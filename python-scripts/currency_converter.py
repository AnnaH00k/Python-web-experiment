# python-scripts/currency_converter.py

import requests
import sys
import json

def convert_currency(api_key, from_currency, to_currency, amount):
    url = f"https://api.exchangerate-api.com/v4/latest/{from_currency}"
    response = requests.get(url)
    data = response.json()
    rate = data['rates'].get(to_currency)
    if rate:
        return amount * rate
    else:
        return None

if __name__ == "__main__":
    api_key = sys.argv[1]  # Not used in this simple script but included for consistency
    from_currency = sys.argv[2]
    to_currency = sys.argv[3]
    amount = float(sys.argv[4])
    converted_amount = convert_currency(api_key, from_currency, to_currency, amount)
    print(json.dumps({'converted_amount': converted_amount}))
