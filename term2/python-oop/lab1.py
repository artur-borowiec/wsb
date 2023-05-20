import math
from math import sqrt

class Zespolona:
    def __init__(self, re, im=0.0):
        self.re = re
        self.im = im
       
    def modul(self):
        return sqrt(self.re**2 + self.im**2)
    
z = Zespolona(3, 4)
print(z.modul())
