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
