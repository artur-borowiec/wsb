import random
import string
import time


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
    start_time = time.time()
    fib_rec(num)
    print(f'fibRec execution time: {time.time() - start_time} seconds')


def measure_fib_iter(num):
    start_time = time.time()
    fib_iter(num)
    print(f'fibIter execution time: {time.time() - start_time} seconds')


def write_random_letters():
    with open("randomnums.txt", "w") as textfile:
        for i in range(100):
            textfile.write(f"{random.choice(string.ascii_uppercase)}\n")


def zad_1_1():
    dane = []
    file = open("dane0.txt")
    numbers = file.read().split()
    for s in numbers:
        dane.append(int(s))
    file.close()

    minimum = 0
    maximum = 0
    for w in range(len(dane)):
        if minimum > dane[w]:
            minimum = dane[w]
        elif maximum < dane[w]:
            maximum = dane[w]
    print(f"min: {minimum}")
    print(f"max: {maximum}")


# load_data()
# zad_1_1()
def zad_2():
    dane = []
    file = open("dane1.txt")
    numbers = file.read().split()
    for s in numbers:
        dane.append(int(s))
    file.close()

    start = time.time()
    selection_sort_2(dane)
    stop = time.time()
    print("--- %s sekund ---" % round(stop - start, 2))


def bubble_sort(dane):
    for j in range(0, len(dane)):
        for i in range(0, len(dane) - 1):
            if dane[i] > dane[i + 1]:
                dane[i], dane[i + 1] = dane[i + 1], dane[i]


def better_bubble_sort(dane):
    for j in range(len(dane) - 1, -1, -1):
        for i in range(0, j):
            if dane[i] > dane[i + 1]:
                dane[i], dane[i + 1] = dane[i + 1], dane[i]


def selection_sort_2(dane):
    for i in range(len(dane)):
        k = i
        for j in range(i + 1, len(dane)):
            if dane[k] > dane[j]:
                k = j
        dane[i], dane[k] = dane[k], dane[j]


def zad3():
    dane = [-5, -3, 0, 235, 2355, 32153]
    lb = 0
    ub = len(dane)-1
    szukam = 235
    while lb <= ub:
        mid = (lb + ub) // 2
        if dane[mid] == szukam:
            print("Znalazłem na pozycji: ", mid)
            break
        elif dane[mid] > szukam:
            ub = mid - 1
        else:
            lb = mid + 1
    if lb > ub:
        print("Nie znalazłem")

zad3()
