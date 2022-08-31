import requests

with open('token') as f:
    telegram_token = f.readline().strip()
    token_currency = f.readline().strip()
    token_crypto_currency = f.readline().strip()
    token_weather = f.readline().strip()
    token_cat = f.readline().strip()
    token_humour = f.readline().strip()
    token_nasa = f.readline().strip()


def currency():
    url = "https://api.apilayer.com/exchangerates_data/latest"
    headers = {'apikey': token_currency}
    params = {'base': 'EUR', 'symbols': 'USD, GBP, CNY'}
    response = requests.get(url=url, headers=headers, params=params).json()
    return f"1 EUR = {response['rates']['USD']} USD\n1 EUR = {response['rates']['GBP']} GBP\n1 EUR = " \
           f"{response['rates']['CNY']} CNY"


def crypto_currency():
    url = 'http://api.coinlayer.com/live'
    params = {'access_key': token_crypto_currency, 'target': 'USD', 'symbols': 'BTC'}
    response = requests.get(url=url, params=params).json()
    return f"1 BTC = {response['rates']['BTC']} USD"


def weather(city):
    url = 'http://api.weatherstack.com/forecast'
    params = {'access_key': token_weather, 'query': city}
    try:
        response = requests.get(url=url, params=params).json()
        answer = f"Current temperature in {params['query']}, {response['location']['country']} = {response['current']['temperature']} Celsius, feels like " \
           f"{response['current']['feelslike']} Celsius. Weather is {response['current']['weather_descriptions'][0]}. Wind speed is " \
                 f"{round(response['current']['wind_speed']/3.6, 1)} m/s"
    except KeyError:
        answer = 'Something is wrong. Try another City'
    return answer


def cat():
    url = 'https://api.thecatapi.com/v1/images/search'
    headers = {'api_key': token_cat}
    params = {'size': 'full'}
    response = requests.get(url=url, headers=headers, params=params).json()
    return response[0]['url']


def memes():
    url = 'https://api.humorapi.com/memes/random'
    params = {'api-key': token_humour, 'media-type': 'image'}
    response = requests.get(url=url, params=params).json()['url']
    return response


def nasa():
    url = 'https://api.nasa.gov/planetary/apod'
    params = {'api_key': token_nasa}
    response = requests.get(url=url, params=params).json()['url']
    return response