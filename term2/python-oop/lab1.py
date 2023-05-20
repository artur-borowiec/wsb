import math
from math import sqrt

class Zespolona:
    def __init__(self, re, im=0.0):
        self.re = re
        self.im = im
        
    def __str__(self):
        return f'{self.re}+{self.im}i'
       
    def modul(self):
        return sqrt(self.re**2 + self.im**2)
    
    @staticmethod
    def dodaj(zesp1, zesp2):
        return Zespolona(zesp1.re+zesp2.re, zesp1.im+zesp2.im)
        
    @staticmethod
    def mnoz(zesp1, zesp2):
        return Zespolona((zesp1.re * zesp2.re) - (zesp1.im * zesp2.im),
            (zesp1.im * zesp2.re) + (zesp1.re * zesp2.im))
    
z1 = Zespolona(3, 4)
z2 = Zespolona(5, 2)
z3 = Zespolona(3, -7)

assert z1.modul() == 5.0
assert str(Zespolona.dodaj(z1, z1)) == "6+8i"
assert str(Zespolona.mnoz(z2, z3)) == "29+-29i"

class FunkcjaKwadratowa:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
        
    def __str__(self):
        return f"{self.a}x^2 + {self.b}x + {self.c}"
        
    def rozwiaz(self):
        d = self.b**2 - 4 * self.a * self.c
        if (d < 0):
            return "Brak miejsc zerowych"
        elif (d == 0):
            return(f"{-self.b / (2*self.a)}")
        else:
            sqd = sqrt(d)
            m1 = (-self.b - sqd) / (2*self.a)
            m2 = (-self.b + sqd) / (2*self.a)
            return f"{m1}, {m2}"
        
        
assert str(FunkcjaKwadratowa(2,3,4)) == "2x^2 + 3x + 4"
fun1 = FunkcjaKwadratowa(2,4,2)
assert str(fun1) == "2x^2 + 4x + 2"
assert fun1.rozwiaz() == '-1.0'
assert FunkcjaKwadratowa(2,1,2).rozwiaz() == "Brak miejsc zerowych"
assert FunkcjaKwadratowa(1,2,-3).rozwiaz() == "-3.0, 1.0"
