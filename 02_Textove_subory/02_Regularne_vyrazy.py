import re
# Priklad 1
# Zistite, či sa v texte nachádza slovo „Python“.
# text = "Mám veľmi rád programovanie v jazyku Python"
# vysledok = re.search(r'Python',text)
# print(vysledok)
# print(vysledok.group())

# Priklad 2
# V texte nájdite slovo, ktoré sa začína na „k“, pokračuje ľubovoľným znakom 
# a končí na „ň“ (napr. koň, kôň).
# text = "Videl som koňa aj kôň, čo sa pasie."
# text = "Alex videl Alexandra."
# vysledok = re.findall(r'k.ň',text)
# vysledok = re.findall(r'A..x',text)
# print(vysledok)

# Priklad 3 
# Nájdite v texte všetky čísla.
# text = "Mám 4 preddmety a 222 žiakov."
# vysledok = re.findall(r'\d',text) #najde cislice jednotlivo
# vysledok = re.findall(r'\d+',text)#najde cislice v celistvosti
# print(vysledok)

# Priklad 4
# Porovnajte, ako sa líšia vzory ba* a ba+ na slovách s rôznym počtom písmena „a“.
# text = "b ba baa baaa"
# vysledok = re.findall(r'ba+',text)
# print(vysledok)
# vysledok = re.findall(r'ba*',text)
# print(vysledok)

# Priklad 5
# Nájdite v texte obidva tvary slova — „color“ aj „colour“.
# text = "Po americky sa píše color, po britsky colour."
# print(re.findall(r'colou?r',text))

# Priklad 6
# Nájdite v slove všetky samohlásky.
# text = "Mám rád programovanie"
# print(re.findall(r'[aeiouyôäáéí]',text))

# Priklad 7
# Zo zmiešaného textu vyberte iba malé písmená.
# text = "Adam je super programátor a Lukáš tiež."
# print(re.findall(r'[a-ž]+',text))

# Priklad 8
# Z textu vyberte všetko, čo NIE je číslica.
# text = "Cena: 25€, zľava 5€"
# # print(re.findall(r'[^0-9]+',text))
# print(re.findall(r'[^\d]+',text))

# Priklad 9
# Rozdeľte vetu na jednotlivé slová bez ohľadu na počet medzier medzi nimi.
# text = "Ahoj kamarát, ako sa máš?"
# # print(re.findall(r'\w+',text))
# # print(re.findall(r'[A-Ž0-9]+',text))
# print(re.findall(r'\s+',text))

# Priklad 10
# Overte, či zadaný reťazec obsahuje IBA číslice — od začiatku až po koniec, 
# nie iba ich časť.
# text = "123456"
# print(re.findall(r'^\d+$',text))

# Priklad 11
# V texte nájdite slovo „mačka“ tak, aby sa nezapočítal jeho výskyt vnútri iného, 
# dlhšieho slova.
# text = "mačka, omačkaná košela"
# print(re.findall(r'\bmačka\b',text))

# Priklad 12
# Overte, či zadané telefónne číslo obsahuje presne 10 číslic.
# cislo = "0910666547"
# if re.fullmatch(r'\d{10}',cislo):
#     print("Ano je to platné číslo.")
# else:
#     print("Nie je platné číslo")

# Priklad 13
# Z dátumu vo formáte DD.MM.RRRR vytiahnite deň, 
# mesiac a rok samostatne.
text = "Narodil som sa 31.02.1978"
zhoda = re.search(r'(\d{2})\.(\d{2})\.(\d{4})',text)
print(zhoda.group(1))
print(zhoda.group(2))
print(zhoda.group(3))

# Priklad 14
# Nájdite v texte slovo „mama“ alebo slovo „otec“.
# text = "Dnes príde mama aj otec."
# print(re.findall(r'mama|otec',text))

# Priklad 16
text = 'Napíš mi na adam.novak@example.com alebo na skolu@gmail.com.'
print(re.findall(r'[\w.]+@[\w-]+\.[a-z]{2,}', text))
