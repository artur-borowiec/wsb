import api
import cvtool


def format_population(population):
    population_in_thousands = int(1000 * population)
    return '{:,}'.format(population_in_thousands).replace(',', ' ')


def run():
    country = cvtool.country_from_file("images/flag.webp")
    response_list = api.country_by_name(country).json()
    response_dict = response_list[0]

    print(f"===== {country} =====")
    print("Capital: " + response_dict["capital"])
    print("Population: " + format_population(response_dict["population"]))
