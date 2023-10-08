import string
from time import time
import random


def fib_rec(n):
    if n <= 2:
        return 1
    else:
        return fib_rec(n - 1) + fib_rec(n - 2)


def fib_iter(n):
    cur = 1
    last = 1
    while n > 2:
        n = n - 1
        cur, last = cur + last, cur - last
    return cur


def measure_fib_rec(num):
    start_time = time()
    fib_rec(num)
    print(f'fibRec execution time: {time() - start_time} seconds')


def measure_fib_iter(num):
    start_time = time()
    fib_iter(num)
    print(f'fibIter execution time: {time() - start_time} seconds')


def write_random_letters():
    with open("randomnums.txt", "w") as textfile:
        for i in range(100):
            textfile.write(f"{random.choice(string.ascii_uppercase)}\n")


dane = []


def load_data():
    file = open("dane0.txt")
    numbers = file.read().split()
    for s in numbers:
        dane.append(int(s))
    file.close()


def zad_1_1():
    minimum = 0
    maximum = 0
    for w in range(len(dane)):
        if minimum > dane[w]:
            minimum = dane[w]
        elif maximum < dane[w]:
            maximum = dane[w]
    print(f"min: {minimum}")
    print(f"max: {maximum}")


load_data()
zad_1_1()
