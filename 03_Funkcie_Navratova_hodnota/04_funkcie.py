from random import *
# Vytvorme funkciu, ktorá nám vráti náhodné 
# písmeno malej abecedy s názvom randchar()

# def randchar():
#     cislo = randint(ord('a'),ord('z'))
#     znak = chr(cislo)
#     return znak
def randchar(): 
    return chr(randint(ord('a'),ord('z')))

def heslo(n):
    heslo = ""
    for i in range(n):
        heslo += randchar()
    return heslo

def x_na_y(x,y):
    return x**y

def rozdel_meno(vstup):
    medzera = vstup.find(" ")
    meno = vstup[:medzera]
    priezvisko = vstup[medzera+1:]
    return meno, priezvisko

# Upravte funkciu rozdelmeno tak, aby fungovala aj v prípade, 
# že celé meno obsahuje viac krstných mien oddelených medzerou 
# a potom priezvisko. Napríklad rozdelí meno 'Adam Ján Múdry'.
def rozdel_meno2(vstup):
    otoceny = vstup[::-1]
    medzera = otoceny.find(" ")
    priezvisko =&
    
    medzera = vstup.find(" ")
    meno = vstup[:medzera]
    priezvisko = vstup[medzera+1:]
    return meno, priezvisko

# print(randchar())
# print(heslo(10))
meno,priezvisko = rozdel_meno("Alexander Oravec")
print(rozdel_meno("Alexander Oravec"))
print(list(rozdel_meno("Alexander Oravec")))
print(meno)
print(priezvisko)