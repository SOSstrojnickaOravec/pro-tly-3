subor = ("Peter", 45, ("Alex", 11, "Milan"))
print(subor[0])
print(subor[0])
print(subor[0])

subor = ("Jozef",) + subor[1::]
print(subor[0])
print(*subor,sep="\n")

for i in subor:
    print(i)

print(subor[2][1])
