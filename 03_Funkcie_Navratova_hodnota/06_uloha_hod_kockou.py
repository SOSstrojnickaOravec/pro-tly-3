# Hod kockou: Vytvorte funkciu hod_kockou() bez parametrov, 
# ktorá vráti náhodné číslo od 1 do 6. Program päťkrát „hodí“ 
# dvomi kockami a vypíše hodené čísla aj ich súčet, napríklad 3 + 5 = 8.
from random import *

def hod_kockou():
    return randrange(1,7)

for i in range(5):
    a = hod_kockou()
    b = hod_kockou()
    sucet = a + b
    print(f"{a} + {b} = {sucet}")
    