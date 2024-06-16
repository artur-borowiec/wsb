import requests


def test_weather_in_city(name):
    endpoint = 'https://api.openweathermap.org/data/2.5/weather'
    params = {
        'q': name,
        'appid': '23fc47171f1bb26ec537d9bf1a271313',
        'units': 'metric'
    }

    response = requests.get(endpoint, params=params)
    json = response.json()

    assert response.status_code == 200, 'Wrong response code'
    assert json['name'] == name, 'Name does not match'
    assert json['visibility'] > 0, 'Visibility invalid'
    assert json['sys']['sunset'] > json['sys']['sunrise'], 'Sun time does not match'
    print('Test for ' + name + ' passed!')


test_weather_in_city('Warsaw')
test_weather_in_city('New York')
