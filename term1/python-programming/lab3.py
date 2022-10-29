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
    guess = int(input("Guess a number: "))
    while guess != num:
        if guess > num:
            guess = int(input("Too high, guess again: "))
        else:
            guess = int(input("Too low, guess again: "))
    print("You guessed correctly")
    
def task58():
    score = 0
    questions_num = 5
    for i in range(questions_num):
        num1 = random.randint(1,20)
        num2 = random.randint(1,20)
        answer = int(input(f"{num1} + {num2} = "))
        if answer == num1+num2:
            print("Right!")
            score+=1
        else: print("Wrong!")
    print(f"You scored {score} points!")
        