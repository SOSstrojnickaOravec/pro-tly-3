# ntica = ("ahoj",45, (14,15))
# zoznam = ["ahoj",45, [14,15]]
# mnozina = {14,48,78}
# slovnik = {"osoba":"Adam",
#            "vek":18,
#            "narodenie":"BnB",
#            "konicky":["filmy","hudba", "zeny"]}
# slovnik["osoba"] = "Martin"
# print(slovnik["osoba"])

import json
osoba = {"meno":"Adam",
           "vek":18,
           "narodenie":"BnB",
           "konicky":["filmy","hudba", "beh"]
           }
with open("osoba.json","w", encoding="utf-8") as subor:
    json.dump(osoba,subor,ensure_ascii=False,indent=2)

with open("osoba.json","r", encoding="utf-8") as subor:
    osoba2 = json.load(subor)

print(osoba)
print(osoba2)
print(f"{osoba2["meno"]} - {osoba2["vek"]} - ",end="")
for konicek in osoba2["konicky"]:
    print(f"{konicek}, ",end="")