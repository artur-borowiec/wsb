import api
import cvtool


def run():
    number_plate = cvtool.number_plate_from_image("images/numberplate.jpg")
    print(number_plate)
