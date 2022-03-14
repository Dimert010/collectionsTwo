import random

def lootje():
    name = {}
    lijst= []
    lijst2 = []
    vraag = int(input("hoeveel namen wilt u invullen?:"))
    for i in range(vraag):
        naam = input("vul hier de namen in: ")
        name[naam]= ""
        lijst.append(naam)
        lijst2.append(naam)
    while len(lijst2) !=0:
        for i in lijst:
            dat = random.choice(lijst2)
            if i != dat:
                name[i] = dat
                lijst2.remove(dat)
            else:
                lijst2 = lijst.copy()
                break

    return name

print(lootje())