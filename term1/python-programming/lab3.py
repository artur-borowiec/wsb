import random

# task 56
def task56():
    num = random.randint(1,10)
    print(num)
    guess = int(input("Guess a number: "))
    while guess != num:
        guess = int(input("Wrong number, guess again: "))
    print("You guessed correctly")
    