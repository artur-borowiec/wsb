import pytesseract
import cv2

pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'


def country_from_file(filename):
    img = cv2.imread(filename)
    return pytesseract.image_to_string(img).strip()


def cities_from_image(filename):
    img = cv2.imread(filename)
    result = pytesseract.image_to_string(img).strip().split('\n')
    return list(filter(len, result))
