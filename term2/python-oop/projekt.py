from datetime import datetime 

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
        return self.kwota/self.zaIleMiesiecy()

w1 = Wydatek(1000, (9, 2023))
w2 = Wydatek(2000, (8, 2023))
w2 = Wydatek(5000, (12, 2024))


assert(w1.zaIleMiesiecy() == 3)
assert(w1.ileMiesiecznie() == 1000/3)
