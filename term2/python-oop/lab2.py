import math
from math import sqrt
from abc import abstractmethod

class Liczba:
    def __init__(self):
        pass
    
    @staticmethod
    @abstractmethod
    def dodaj(l1, l2):
        pass
    
    @staticmethod
    @abstractmethod
    def mnoz(l1, l2):
        pass

class Zespolona(Liczba):
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

class Calkowita(Liczba):
    
    def __init__(self, val):
        self.val = val
        
    def __eq__(self, other):
        return self.val == other.val
        
    @staticmethod
    def dodaj(l1, l2):
        return Calkowita(l1.val + l2.val)
        
    @staticmethod
    def mnoz(l1, l2):
        return Calkowita(l1.val * l2.val)
        
    @staticmethod
    def odejmij(l1, l2):
        return Calkowita(l1.val - l2.val)
        
    @staticmethod
    def dziel(l1, l2):
        return Calkowita(l1.val / l2.val)
        
c1 = Calkowita(10)
c2 = Calkowita(2)

assert Calkowita.mnoz(c1, c2) == Calkowita(20)
assert Calkowita.dziel(c1, c2) == Calkowita(5)
assert Calkowita.dodaj(c1, c2) == Calkowita(12)
assert Calkowita.odejmij(c1, c2) == Calkowita(8)

class Funkcja:
    @abstractmethod
    def __init__(self):
        pass
        
    @abstractmethod
    def rozwiaz(self):
        pass
        
class FunkcjaLiniowa(Funkcja):
    def __init__(self, a, b):
        self.a = a
        self.b = b

class FunkcjaKwadratowa(Funkcja):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
        
    def __str__(self):
        str = ""
        if (self.a != 0):
            str += f"{self.a}x^2 + "
        str += f"{self.b}x + {self.c}"
        return str
        
    def rozwiaz(self):
        if (self.a == 0):
            if (self.b == 0):
                if (self.c == 0):
                    return "∞ rozwiazan"
                else:
                    return "Brak rozwiazan"
            else:
                return f"{-self.c / self.b}"
        d = self.b**2 - 4 * self.a * self.c
        if (d < 0):
            return "Brak rozwiazan"
        elif (d == 0):
            return(f"{-self.b / (2*self.a)}")
        else:
            sqd = sqrt(d)
            m1 = (-self.b - sqd) / (2*self.a)
            m2 = (-self.b + sqd) / (2*self.a)
            return f"{m1}, {m2}"
            
class FunkcjaLiniowa(FunkcjaKwadratowa):
    def __init__(self, a, b):
        FunkcjaKwadratowa.__init__(self, 0, a, b)
        
assert str(FunkcjaKwadratowa(2,3,4)) == "2x^2 + 3x + 4"
fun1 = FunkcjaKwadratowa(2,4,2)
assert str(fun1) == "2x^2 + 4x + 2"
assert fun1.rozwiaz() == '-1.0'
assert FunkcjaKwadratowa(2,1,2).rozwiaz() == "Brak rozwiazan"
assert FunkcjaKwadratowa(1,2,-3).rozwiaz() == "-3.0, 1.0"

funL = FunkcjaLiniowa(2,5)
assert str(funL) == "2x + 5"
assert funL.rozwiaz() == "-2.5"

funL2 = FunkcjaLiniowa(0,3)
assert funL2.rozwiaz() == "Brak rozwiazan"

funL3 = FunkcjaLiniowa(3,0)
assert funL3.rozwiaz() == "0.0"

funL4 = FunkcjaLiniowa(0,0)
assert funL4.rozwiaz() == "∞ rozwiazan"
