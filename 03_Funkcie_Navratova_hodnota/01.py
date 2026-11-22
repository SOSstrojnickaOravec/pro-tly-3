# zadanie - Zadam pocet cisel a potom vypise sucet cisel ktore zadam
from random import *

def sucet(a,b):
    return a+b

def obsah_stvorca(a):
    return a*a

def kvadrat(a,b,c):
    D = (b**2) -(4*a*c)
    if D <0: return "Rovnica nemá riešenie"
    if D==0 : return (-b)/(2*a)
    if D> 0 : return [(-b+(D)**(1/2))/(2*a),(-b-(D)**(1/2))/(2*a)]

# print(sucet(randrange(101),randrange(101)))
# print("Obsah stvorca", obsah_stvorca(5))

print(kvadrat(5,4,-9))
print(kvadrat(3,7,2))
print(kvadrat(2,4,2))
print(kvadrat(2,4,15))