from datetime import datetime 
import math

def diff_month(d1, d2):
    return (d1.year - d2.year) * 12 + d1.month - d2.month
    
class Wydatek:
    def __init__(self, kwota, data):
        self.kwota = kwota
        self.data = datetime(data[1], data[0], 1)
    
    def __str__(self):
        return f"Wydatek: {self.kwota}PLN dnia {self.data}"
        
    def zaIleMiesiecy(self):
        return diff_month(self.data, datetime.today())
        
    def ileMiesiecznie(self):
        return math.ceil(self.kwota/self.zaIleMiesiecy())

class Wydatki:
    def __init__(self):
        self.lista = []
        
    def dodajWydatek(self, wydatek):
        self.lista.append(wydatek)
        
    def wypiszWszystkie(self):
        for w in self.lista:
            print(w)
    
    def ileMiesiecznie(self):
        suma = 0
        for w in self.lista:
            suma += w.ileMiesiecznie()
        return suma

w1 = Wydatek(1000, (8, 2023))
w2 = Wydatek(2000, (10, 2023))
w3 = Wydatek(5000, (4, 2024))

assert(w1.zaIleMiesiecy() == 2)
assert(w1.ileMiesiecznie() == 500)

wydatki = Wydatki()
wydatki.dodajWydatek(w1)
wydatki.dodajWydatek(w2)
wydatki.dodajWydatek(w3)
wydatki.wypiszWszystkie()

assert(len(wydatki.lista) == 3)
assert(wydatki.ileMiesiecznie() == 1500)
