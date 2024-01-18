import re

import cvtool


def is_polish_plate(plate_number):
    polish_plate_pattern = re.compile(r'^[A-Z]{3}\s[A-Z0-9]{0,5}$')
    is_polish = bool(polish_plate_pattern.match(plate_number))

    return 'Poprawny format polskiej tablicy' if is_polish else 'Tablica niepoprawna!'


def run():
    number_plate = cvtool.number_plate_from_image("images/numberplate.jpg")

    print(number_plate)
    print(is_polish_plate(number_plate))
