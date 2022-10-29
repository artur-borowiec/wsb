import random

def task56():
    num = random.randint(1,10)
    print(num)
    guess = int(input("Guess a number: "))
    while guess != num:
        guess = int(input("Wrong number, guess again: "))
    print("You guessed correctly")
    
def task57():
    num = random.randint(1,10)
    print(num)
    guess = int(input("Guess a number: "))
    while guess != num:
        if guess > num:
            guess = int(input("Too high, guess again: "))
        else:
            guess = int(input("Too low, guess again: "))
    print("You guessed correctly")
    