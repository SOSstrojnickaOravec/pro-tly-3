from random import *
# subor = open("text.txt","w")
# subor.write("Ahoj\n")
# subor.write("="*20)
# subor.write("\nAhoj\n")
# subor.write("Ahoj\n")
# print("Ahojkyyyy",file=subor)
# subor.close()

# subor = open("text1.txt","w")
# for i in range(10):
#     for j in range(10):
#         print(j+1,end=" ",file=subor)
#     print("",file=subor)
# subor.close()

# Vytvorte program, ktorý do textového súboru zapíše tabuľku 
# kódovania znakov malej abecedy. Na samostatnom riadku bude kód 
# písmena abecedy, medzera a znak.
# subor = open('tabulka.txt', 'w')
# for i in range(ord("a"), ord("z")):
#     # subor.write(str(i) + ' ' + chr(i) + '\n')
#     print(str(i) + ' ' + chr(i),file=subor)
# subor.close()

# Vytvorte program, ktorý do textového súboru vygeneruje 
# zadaný počet náhodných hesiel. Heslo má práve 8 znakov 
# a skladá sa len z písmen malej abecedy.

# Vytvorte program, ktorý do textového súboru vygeneruje zadaný 
# počet náhodných hesiel. Heslo má na začiatku 3 čísla potom 
# 8 znakov malej abecedy a 3 špeciálne znaky.
# pocet = int(input("Zadaj počet hesiel:"))
# def nahodne_heslo(subor):
#     heslo = ""
#     for i in range(3):
#         heslo += chr(randint(48,57))
#     for i in range(8):
#         heslo += chr(randint(ord("a"),ord("z")))
#     for i in range(3):
#             heslo += chr(randint(33,47))
#     print(heslo,file=subor)

# subor = open("hesla.txt","w")
# for i in range(pocet):
#     nahodne_heslo(subor)
# subor.close()

# import random
# import string

# POCET_CISEL = 3
# POCET_PISMEN = 8
# POCET_SPEC = 3
# SPECIALNE = "!@#$%&*+-?"

# def vygeneruj_heslo():
#     heslo  = "".join(random.choices(string.digits, k=POCET_CISEL))
#     heslo += "".join(random.choices(string.ascii_lowercase, k=POCET_PISMEN))
#     heslo += "".join(random.choices(SPECIALNE, k=POCET_SPEC))
#     return heslo

# pocet = int(input("Zadaj počet hesiel: "))

# with open("hesla.txt", "w", encoding="utf-8") as subor:
#     for _ in range(pocet):
#         subor.write(vygeneruj_heslo() + "\n")

# print(f"Do súboru hesla.txt bolo zapísaných {pocet} hesiel.")

# import random, string

# def heslo():
#     return ("".join(random.choices(string.digits, k=3))
#           + "".join(random.choices(string.ascii_lowercase, k=8))
#           + "".join(random.choices("!@#$%&*+-?", k=3)))

# pocet = int(input("Zadaj počet hesiel: "))

# with open("hesla.txt", "w") as f:
#     f.writelines(heslo() + "\n" for _ in range(pocet))

text = input("Zadaj odkaz pre budúcnosť: ")
while text !="koniec":
    if text =="delete":
        subor = open("buducnost.txt", "w")
        subor.close()
    elif text !="":
        subor = open("buducnost.txt", "a")
        print(text,file=subor)
        subor.close()
    text = input("Zadaj odkaz pre budúcnosť: ")
    