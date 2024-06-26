import random
import array

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

def task59():
    colors = ["red", "blue", "black", "white", "green"]
    sentences = [
        "You were caught RED handed",
        "You are probably feeling BLUE right now",
        "Don't be a BLACK sheep in the herd",
        "Don't tell me this WHITE lie",
        "I bet you are GREEN with envy"
    ]
    pickedByCpu = colors[random.randint(0,4)]
    chosenColor = chooseAColor()
    choice = colors.index(chosenColor)
    while chosenColor != pickedByCpu:
        print(sentences[choice])
        chosenColor = chooseAColor()
        choice = colors.index(chosenColor)
    print("Well done")

def chooseAColor():
    return input("Pick one of colors (red, blue, black, white, green): ").lower()
    
def task69():
    countries = ("Poland", "Germany", "Slovakia", "Hungary", "Greece")
    print(countries)
    choice = input("Choose a country: ")
    print(countries.index(choice))

def task70():
    countries = ("Poland", "Germany", "Slovakia", "Hungary", "Greece")
    print(countries)
    choice = int(input("Choose a country (0-4): "))
    print(countries[choice])
    
def task71():
    sports = ["football", "table tennis"]
    sport = input("What's your favorite sport?: ")
    sports.append(sport)
    sports.sort()
    print(sports)
    
def task72():
    subjects = ['maths', 'arts', 'english', 'french', 'physics', 'chemistry']
    print(subjects)
    notLiked = input("What subject you don't enjoy? ")
    subjects.remove(notLiked.lower())
    print(subjects)
    
def task87():
    word = input("Write a word: ")[::-1]
    for i in (range(len(word))):
        print(f"{word[i]}")
        
def task94():
    numbers = array.array('i', [1, 2, 3, 4, 5])
    choice = int(input("Choose a number: "))
    while choice not in numbers:
        choice = int(input("Try again: "))
    print(numbers.index(choice))
        
def task106():
    file = open("Names.txt", "w")
    names = ["John", "Anne", "Michael", "Dwight", "Kevin"]
    for i in range(len(names)):
        file.write(f"{names[i]}\n")
    file.close()

def task107():
    file = open("Names.txt", "r")
    print(file.read())
    file.close()        
        