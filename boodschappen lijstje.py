lijst = []
def bodschaplijst():
    bd = True
    while bd == True:
        vraag = input("wat heb je nodig?: ")
        if vraag == "stop":
            bd = False
        else:
            lijst.append(vraag)
    return lijst
print(bodschaplijst())