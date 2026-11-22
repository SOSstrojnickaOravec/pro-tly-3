# Typ trojuholníka: Vytvorte logickú funkciu existuje(a, b, c) 
# (trojuholník existuje, ak je súčet každých dvoch strán väčší 
#  ako tretia strana) a funkciu typ_trojuholnika(a, b, c), ktorá 
# vráti jeden z reťazcov: 'neexistuje', 'rovnostranný', 'rovnoramenný', 'rôznostranný'.

def je_trojuholnik(a,b,c):
    if ((a+b>c) and(a+c>b) and (b+c>a)):
        return True
    else: return False

def typ(a,b,c):
    if a == b == c:
        return "Je rovnostranny"
    elif a == b
if (je_trojuholnik(10,2,5)) :
    print("Je trojuholnik")
else:
    print("Nie je trojuholnik")

