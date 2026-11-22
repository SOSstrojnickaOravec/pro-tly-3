import csv

with open("ziaci.csv","r",encoding="utf-8",newline="") as subor:
    nacitanie = csv.DictReader(subor)
    for riadok in nacitanie:
        # print(riadok)
        print(f"{riadok['meno']} - {riadok["priezvisko"]} - {riadok["trieda"]}")