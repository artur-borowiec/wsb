import pytesseract
import cv2
import easyocr

pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'


def country_from_file(filename):
    img = cv2.imread(filename)
    return pytesseract.image_to_string(img).strip()


def cities_from_image(filename):
    reader = easyocr.Reader(['en'])
    result = reader.readtext(filename)
    cities = [item[1] for item in result]

    return cities


def number_plate_from_image(filename):
    reader = easyocr.Reader(['en'])
    result = reader.readtext(filename)
    return result[1][1]


def shopping_list_from_image(filename):
    reader = easyocr.Reader(['en'])
    result = reader.readtext(filename)
    labels = [item[1] for item in result]
    pairs = [(labels[i], labels[i + 1]) for i in range(0, len(labels) - 1, 2)]

    return pairs


def prescription_from_image(filename):
    reader = easyocr.Reader(['pl'])
    result = reader.readtext(filename)
    labels = [item[1] for item in result]

    return labels
