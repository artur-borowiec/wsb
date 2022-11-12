import string
import random
import re
import datetime

# 1.
def random_password():
    l = int(input("Password length: "))
    p = ""
    for i in range(l):
        p += random.choice(string.ascii_letters)
    print(p)
    
# 2. password validator - number, special char, capital letter
def password_valid():
    p = input("Enter password: ")
    print(
        any(t in string.digits for t in p)
        and any(t in string.punctuation for t in p)
        and len(p) >= 8)

# 3. Letters in a word
def letters_in_word(w):
    l = set(list(w))
    print(l)
    
# 4. gas cost
def calculate_gas_cost():
    s = float(input("Consumption "))
    c = float(input("Cena paliwa "))
    d = int(input("Dystans "))
    print(d/100 * s * c)

# 8. phone number censoring
def censore_phone():
    t = input("Selling ad: ")
    print(re.sub(r"[\d]{9}", "*********", t))

# 9. PESEL -> gender
def gender_from_pesel():
    p = input("PESEL: ")
    if (len(p) != 11): return
    g = "k" if int(p[9])%2 == 0 else "m"
    print(g)

#10. Sumowanie liczb aż wprowadzona nieliczba

#12. Przebieg samochodu z mil do km
def odometer_in_miles_to_km():
    odoM = int(input("Odometer in miles: "))
    rate = 1.609344
    print(int(odoM*rate))
    
#14. Zegar binarny
#15. Krokomierz do km
def steps_to_km():
    s = int(input("Steps: "))
    print(f"{s*0.00064}km")

#17. Fizzbuzz
def fizzbuzz():
    n = int(input("Run fizzbuzz for number: "))
    for i in range(1, n+1):
        if(i%3==0 and i%5==0): print("fizzbuzz")
        elif(i%3==0): print("fizz")
        elif(i%5==0): print("buzz")
        else: print(i)
        
#19. Zysk z lokaty
#20. Orzeł reszka
def head_or_tails():
    ht = input("[h]ead or [t]ails? ")
    is_same = random.choice(['h', 't']) == ht
    print("Yes!") if is_same else print("No!")

#
##20. A is % percent of b
#print("Give me 2 numbers")
#a = int(input("int1 = "))
#b = int(input("int2 = "))
#print(f"a is {a/b*100} % of b")
#
##21. today's weekday
#from datetime import date
#print(date.today().strftime('%A'))
#
##22. PESEL -> birth weekday
def birth_weekday():
    p = input("Pesel:")
    a = p[0:6]
    date = datetime.datetime.strptime(a, '%Y%m%d')
    print(date.strftime('%A'))
    
##23. lotto
def lotto():
    p = int(input("Lotto for x numbers: "))
    for i in range(p):
        print(random.randint(1, 49))
        
# 24.
def next_elections_president():
    n = datetime.datetime.today().year
    until = 5-n%5
    print(n+until)
    
# 25
def until_end_of_year():
    today = datetime.date.today()
    current_y = today.year
    end = datetime.date(current_y,12,31)
    diff = end - today
    print (diff.days)


choice = int(input("Choose task:"))
taskDict = {
    1: random_password,
    2: password_valid,
    3: letters_in_word,
    4: calculate_gas_cost,
    8: censore_phone,
    9: gender_from_pesel,
    12: odometer_in_miles_to_km,
    15: steps_to_km,
    17: fizzbuzz,
    20: head_or_tails,
    22: birth_weekday,
    23: lotto,
    24: next_elections_president,
    25: until_end_of_year
}[choice]()
