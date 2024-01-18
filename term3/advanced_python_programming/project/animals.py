from collections import Counter
import cvtool
import matplotlib.pyplot as plt


def run():
    input_array = cvtool.animals_from_image('images/animals.png')
    occurrence_count = Counter(input_array)
    result_pairs = list(occurrence_count.items())
    elements, counts = zip(*result_pairs)

    plt.bar(elements, counts)
    plt.ylabel('Occurences')
    plt.show()
