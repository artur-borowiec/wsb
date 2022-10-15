# task32
import math
r = float(input("Cylinder radius:\n"))
d = float(input("Cylinder depth:\n"))
v = math.pi * (r**2) * d
print(round(v, 3))

# task33
a = int(input("Enter a number:\n"))
b = int(input("Enter another number:\n"))
ans1 = a // b
ans2 = a % b
print(f"{a} divided by {b} is {ans1} with {ans2} remaining")

# task34
print("1) Square\n2) Triangle")
choice = int(input("Enter a number: "))
if choice > 2:
    print("Incorrect option")
elif choice == 1:
    side = float(input("Enter side length: "))
    print(f"Area of square is {side**2}")
else:
    base = float(input("Enter base length: "))
    height = float(input("Enter height: "))
    area = base*height / 2
    print(f"Area of triangle is {area}")

# task35
repeats = 3
name = input("Tell me your name: ")
for i in range(0, repeats):
    print(name)

# task36
name = input("Tell me your name: ")
repeats = int(input("Tell me a number: "))
for i in range(0, repeats):
    print(name)
    
# task37
name = input("Tell me your name: ")
for letter in name:
    print(letter)
    
# task38
repeats = int(input("Tell me a number: "))
name = input("Tell me your name: ")
for i in range(repeats):
    for letter in name:
        print(letter)
    
# task40
number = int(input("Tell me a number below 50:"))
current = 50
while number <= current:
    print(f"{current}")
    current -= 1
    
# task41
name = input("Tell me your name: ")
repeats = int(input("Tell me a number: "))
if repeats < 10:
    for i in range(repeats):
        print(name)
else:
    for i in range(3):
        print("Too much")

# task42
total = 0
for i in range(5):
    num = int(input("Enter a number: "))
    answer = input("Include in total (y/N)? ")
    if answer == "y":
        total += num
print(f"Sum is {total}")

# task43
direction = input("Enter direction (up/down): ")
if direction == "up":
    num = int(input("Tell me a number: "))
    current = 1
    for i in range(num):
        print(current)
        current += 1
elif direction == "down":
    num = int(input("Tell me a number below 20: "))
    current = num
    for i in range(num):
        print(current)
        current -= 1
else:
    print("I don't understand")

# task44
people_number = int(input("How many people to invite?: "))
if people_number < 10:
    for i in range(people_number):
        name = input("Name: ")
        print(f"{name} has been invited")
else:
    print("Too many people")

# task45
total = 0
while total <= 50:
    num = int(input("Enter a number: "))
    total += num
    print(f"Total is {total}")

# task46
num = 0
while num <= 5:
    num = int(input("Enter a number: "))
print(f"The last number you entered is: {num}")

# task47
total = int(input("Enter a number: "))
choice = "y"
while choice == "y":
    num = int(input("Enter a number: "))
    total += num
    choice = input("Do you want to enter another number (y/n)? ")
print(f"Total is {total}")

# task48
total = 0
choice = "y"
while choice == "y":
    name = input("Enter name: ")
    total += 1
    choice = input("Do you want to invite more people (y/n)? ")
print(f"You invited {total} people")

# task50
num = 0
while num < 10 or num > 20:
    num = int(input("Enter a number: "))
    if num < 10:
        print("Too low")
    elif num > 20:
        print("Too high")
print(f"Thank you")

