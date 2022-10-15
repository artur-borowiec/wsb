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
