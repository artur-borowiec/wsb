import requests

api_key = "YTtaM/AAu/ARYhSIyjXpag==VW6oMSowX1Ks0ssl"
timeout = 10


def country_by_name(name):
    api_url = f'https://api.api-ninjas.com/v1/country?name={name}'
    return requests.get(api_url, headers={'X-Api-Key': api_key}, timeout=timeout)


def city_by_name(name):
    api_url = f'https://api.api-ninjas.com/v1/city?name={name}'
    return get(api_url).json()[0]


def get(url):
    return requests.get(url, headers={'X-Api-Key': api_key}, timeout=timeout)
