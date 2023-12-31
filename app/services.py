import requests


def convert_currency(to_currency, from_currency, amount_currency):
    """Конвертируем валюту на внешнему API"""
    url = f"https://api.apilayer.com/exchangerates_data/convert?to={to_currency}&from={from_currency}&amount={amount_currency}"
    # to_currency - основная валюта
    # from_currency - валюта для перевода
    # amount_currency - количество валюты
    headers = {
        "apikey": "otufrS7b3JIM5cipakQfRuE1kXSGxJIT"
    }
    response = requests.request("GET", url, headers=headers)
    data = response.json()
    return data['result']  # выводит {'result' : значение}
