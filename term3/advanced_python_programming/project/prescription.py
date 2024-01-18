import cvtool
import re


def run():
    content = cvtool.prescription_from_image('images/prescription.webp')

    # get indices of prescription headers
    pattern = re.compile(r'Recepta \d+')
    presc_indices = [i for i, text in enumerate(content) if pattern.match(text)]

    # each prescription has 5 elements
    prescriptions = [content[i:i + 5] for i in presc_indices]
    print_prescriptions(prescriptions)


def print_prescriptions(prescriptions):
    for ps in prescriptions:
        print('========')
        print('\n'.join(map(str, ps)))
        print('========')

