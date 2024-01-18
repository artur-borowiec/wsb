import cvtool
import matplotlib.pyplot as plt


def run():
    results = cvtool.shopping_list_from_image('images/shopping.png')
    print(results)
    prices = [float(result[1].replace(',', '.')) for result in results]
    labels = [result[0] for result in results]
    plt.pie(prices, labels=labels, autopct='%1.1f%%')
    plt.axis('equal')
    plt.show()
