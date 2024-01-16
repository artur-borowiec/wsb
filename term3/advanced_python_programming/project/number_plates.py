import re

import cvtool


def is_polish_plate(plate_number):
    polish_plate_pattern = re.compile(r'^[A-Z]{3}\s[A-Z0-9]{0,5}$')

    return bool(polish_plate_pattern.match(plate_number))


def run():
    number_plate = cvtool.number_plate_from_image("images/numberplate.jpg")

    print(number_plate, is_polish_plate(number_plate))
