import requests

endpoint = 'http://api.openweathermap.org/data/2.5/weather'
params = {
    'q': 'Warsaw',
    'appid': '',
    'units': 'metric'
}

response = requests.get(endpoint, params=params)
print(response)
