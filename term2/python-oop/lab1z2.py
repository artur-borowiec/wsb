# zad9 - po dodaniu konstruktora widac wszystkie jego wywolania, takze w poprzednich zadaniach. Jesli funkcja zwracala nowy obiekt ze wspolrzednymi, takze widac takie wywolanie.

# zad10 - wywolanie pustego konstruktora powoduje blad TypeError. Spowodowane jest to faktem, ze argumenty x i y konstruktora sa wymagane.

class Punkt:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        print(f"Utworzono punkt ({self.x}, {self.y})")
        
    def wyswietl(self):
        print(f'({self.x}, {self.y})')
        
    def pobierzX(self):
        return self.x
        
    def pobierzY(self):
        return self.y
        
#    def ustawXY(self, x, y):
#        self.x = x
#        self.y = y
        
    def ustawXY(self, p):
        self.x = p.x
        self.y = p.y
        
    def pobierzWsp(self):
        return Punkt(self.x, self.y)
    
# 1
p1 = Punkt(1,2)
p2 = Punkt(4,5)

# 2
print(f"Wspolrzedne punktu p1 to ({p1.x}, {p1.y})")
print(f"Wspolrzedne punktu p2 to ({p2.x}, {p2.y})")

# 3
p1.wyswietl()
p2.wyswietl()

# 4
assert p1.pobierzX() == 1
assert p2.pobierzY() == 5

# 6
# p1.ustawXY(7,8)
# assert p1.pobierzX() == 7
# assert p1.pobierzY() == 8

# 7
p1.ustawXY(Punkt(8,9))
assert p1.pobierzX() == 8
assert p1.pobierzY() == 9

# 8
assert p1.pobierzWsp().x == 8
assert p1.pobierzWsp().y == 9

# 9
Punkt(10, 20)
Punkt(20, 30)

# 10
#p3 = Punkt()
