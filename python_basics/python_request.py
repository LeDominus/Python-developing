import requests # type: ignore

# Указываю URL
url = "https://api.binance.com/api/v3/ticker/price"

# Пишу код для запроса на сервер по URL
response = requests.get(url, params= {'symbol': 'ETHUSDT'})

# Делаю проверку
if response.status_code == 200:
    print(response.json())
else:
    print(f"Ошибка: " + response.status_code )

