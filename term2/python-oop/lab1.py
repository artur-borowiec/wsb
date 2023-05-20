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
print(z1.modul())
print(Zespolona.dodaj(z1,z1))
print(Zespolona.mnoz(z2,z3))
