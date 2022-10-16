# task1
# name = input("What's your name?\n")
# print("Hello", name)

# task2
# name = input("What's your name?")
# surname = input("What's your surname?")
# print("Hello ", name, surname)

# task3
# print("What do you call a bear with no teeth?\nA gummy bear!")

# task4
# num1 = int(input("Tell me 1st number: "))
# num2 = int(input("Tell me 2nd number: "))
# print("The total is", num1+num2)

# task5
# num1 = int(input("Tell me 1st number: "))
# num2 = int(input("Tell me 2nd number: "))
# num3 = int(input("Tell me 3rd number: "))
# answer = (num1 + num2) * 3
# print("The answer is", answer)

# task6
# total = int(input("How many slices of pizza have you started with?\n"))
# eaten = int(input("How many slices of pizza have you eaten?\n"))
# print("There are", total-eaten, "slices left")

# task7
# name = input("What's your name?\n")
# age = int(input("What's your age?\n"))
# print(name, "next birthday you will be", age+1)

# task8
# totalPrice = float(input("What's the total price?\n"))
# diners = int(input("How many diners are there?\n"))
# print("Each person needs to pay", "%.2f" % (totalPrice / diners))

# task9
# days = int(input("Number of days: "))
# hours = days * 24
# minutes = hours * 60
# seconds = minutes * 60
# print(days, "days are", hours, "hours, ", minutes, "minutes or ", seconds, "seconds")

# task10
# kilograms = float(input("Enter weight: "))
# print(kilograms, "kg is", kilograms * 2.204, "pounds")

# task11
# bigNumber = int(input("Enter number over 100: "))
# smallNumber = int(input("Enter number over 100: "))
# print(smallNumber, "can fit", bigNumber//smallNumber, "times in", bigNumber)

# task12
# num1 = int(input("Tell me 1st number: "))
# num2 = int(input("Tell me 2nd number: "))
# print(num2, num1) if num1 > num2 else print(num1, num2)

# task13
# num = int(input("Tell me a number under 20: "))
# print("Thank you") if num < 20 else print("Too high")

# task14
# num = int(input("Tell me a number between 10 and 20: "))
# print("Thank you") if 10 <= num <= 20 else print("Incorrect answer")

# task15
# color = input("Tell me your favorite color: ")
# print("I like red too") if color.lower() == "red" else print("I don't like %s, I prefer red" % color)

# task16
# isRaining = input("Is it raining?\n").lower() == "yes"
# if not isRaining:
#     print("Enjoy your day")
# else:
#     isWindy = input("Is it windy?\n").lower() == "yes"
#     print("It is too windy for an umbrella") if isWindy else print("Take an umbrella")

# task17
# age = int(input("Tell me your age: "))
# if age >= 18:
#     print("You can vote")
# elif age == 17:
#     print("You can learn to drive")
# elif age == 16:
#     print("You can buy a lottery ticket")
# else:
#     print("You can go trick-or-treating")

# task18
# num = int(input("Tell me a number: "))
# if num < 10:
#     print("Too low")
# elif 10 <= num <= 20:
#     print("Correct")
# else:
#     print("Too high")

# task19
# num = int(input("Enter 1, 2 or 3: "))
# if num == 1:
#     print("Thank you")
# elif num == 2:
#     print("Well done")
# elif num == 3:
#     print("Correct")
# else:
#     print("Error message")

# task20
# name = input("What's your name?\n")
# print("Your name length is", len(name))

# task21
#name = input("What's your name?\n")
#surname = input("What's your surname?\n")
#fullname = name + " " + surname
#print(fullname + ", length is", len(fullname))

# task22
#name = input("What's your name in lowercase?\n")
#surname = input("What's your surname in lowercase?\n")
#fullname = f"{name} {surname}"
#print(fullname.title())

# task23
#line = input("Enter a line of nursery rhyme\n")
#start = int(input("Enter start position\n"))
#end = int(input("Enter end position\n"))
#print(line[start:end])

# task24
#word = input("Enter a word\n")
#print(word.upper())

# task25
#name = input("What's your name?\n")
#if len(name) > 5:
#    print(name.lower())
#else:
#    surname = input("What's your surname?\n")
#    print((name+surname).upper())

# task26
#vowels = ['a', 'e', 'i', 'o', 'u']
#word = input("Tell me a word:\n").lower()

#if word[0] in vowels:
#  print(f"{word}way")
#else:
#  print(f"{word[1:]}{word[0]}ay")

# task27
#num = float(input("Tell me a number with lots of decimal places\n"))
#print(num * 2)

# task28
#num = float(input("Tell me a number with lots of decimal places\n"))
#print("%.2f" % (num*2))

# task29
#import math
#num = int(input("Tell me a number over 500\n"))
#print("%.2f" % math.sqrt(num))

# task30
#import math
#print("%.5f" % math.pi)

# task31
#import math
#radius = float(input("Enter a radius of a circle:\n"))
#area = math.pi * radius**2
#print(area)
