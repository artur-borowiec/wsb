from time import time


def fibRec(n):
    if n <= 2:
        return 1
    else:
        return fibRec(n - 1) + fibRec(n - 2)


def fibIter(n):
    cur = 1
    last = 1
    while n > 2:
        n = n - 1
        cur, last = cur + last, cur - last
    return cur


def main():
    num = 500
    measureFibIter(num)

def measureFibRec(num):
    start_time = time()
    fibRec(num)
    print(f'fibRec execution time: {time() - start_time} seconds')

def measureFibIter(num):
    start_time = time()
    fibIter(num)
    print(f'fibIter execution time: {time() - start_time} seconds')


if __name__ == "__main__":
    main()
