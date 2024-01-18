import cv2


def run():
    image = cv2.imread('images/qr.png')
    detector = cv2.QRCodeDetector()
    data, a, b = detector.detectAndDecode(image)
    print(data)
