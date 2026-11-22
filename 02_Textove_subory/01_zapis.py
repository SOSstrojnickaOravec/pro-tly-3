# meno = "Pavol"
# vek = 11.7458785

# with open("poznamky.txt","w",encoding="utf-8") as subor:
#     subor.write("Prvý záznam\n")
#     subor.write("Druhý záznam záznam\n")
    
#     print(meno,"má",vek,"rokov",file=subor)
#     subor.write(meno + " má "+ str(vek) + " rokov\n")
#     print(f"{meno} má {vek:09.0f} rokov.",file=subor)
    
#     print(f"Tretí záznam", file=subor, end="")
#     print(f"Štvrtý záznam",file=subor)

# nakup = ["mlieko","vajcia","chlieb","maslo"]
# with open("nakupny_zoznam.txt","w",encoding="utf-8") as subor:
#     for i, polozka in enumerate(nakup,start = 1):
#         print(f"{i}.{polozka}",file=subor)

# Vytvorte súbor trieda.txt s údajmi troch spolužiakov vo formáte 
# „Meno: Ján, Priemer: 1.67“ — použite f-string s formátovaním 
# priemeru na 2 desatinné miesta.

# meno1 = "Adam"
# meno2 = "Martin"
# meno3 = "Ján"
# priemer1 = 1.67
# priemer2 = 2.33
# priemer3 = 1.0
# with open("trieda.txt","w",encoding="utf-8") as subor:
#     print(f"Meno: {meno1}, Priemer: {priemer1:.2f}",file=subor)
#     print(f"Meno: {meno2}, Priemer: {priemer2:.2f}",file=subor)
#     print(f"Meno: {meno3}, Priemer: {priemer3:.2f}",file=subor)


# ziaci = [("Adam",1.67),("Martin",2.33),("Ján",1.0)]
# with open("trieda.txt","w",encoding="utf-8") as subor:
#     for meno, priemer in ziaci:
#         print(f"Meno: {meno}, Priemer: {priemer:.2f}",file=subor)
        
# Vytvorte program, ktorý pomocou slovníka 
# (napr. {'Pondelok': 'Matematika', 'Utorok': 'Informatika'}) 
# vygeneruje súbor rozvrh.txt, kde na každom riadku bude deň a predmet 
# oddelené f-stringom vo formáte „Pondelok — Matematika“.

rozvrh = {'Pondelok': 'Matematika', 'Utorok': 'Informatika', 'Streda':'Biológia'}
with open("rozvrh.txt", "w", encoding="utf-8") as subor:
    for den, predmet in rozvrh.items():
        print(f"{den} - {predmet}",file=subor)