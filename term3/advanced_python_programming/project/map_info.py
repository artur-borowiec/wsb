import api
import cvtool


def run():
    cities = cvtool.cities_from_image("map.png")

    for city in cities:
        response = api.city_by_name(city)
        print(f"{response['name']} {response['latitude'], response['longitude']}")
