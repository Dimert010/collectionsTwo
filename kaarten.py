import random

def kaartspel():
    harten = ['harten 2', 'harten 3', 'harten 4', 'harten 5', 'harten 6', 'harten 7', 'harten 8', 'harten 9', 'harten 10', "harten boer", "harten vrouw", "harten heer", "harten aas"]
    schoppen = ['schoppen 2', 'schoppen 3', 'schoppen 4', 'schoppen 5', 'schoppen 6', 'schoppen 7', 'schoppen 8', 'schoppen 9', 'schoppen 10', "schoppen boer", "schoppen vrouw", "schoppen heer", "schoppen aas"]
    klaver = ['klaver 2', 'klaver 3', 'klaver 4', 'klaver 5', 'klaver 6', 'klaver 7', 'klaver 8', 'klaver 9', 'klaver 10', "klaver boer", "klaver vrouw", "klaver heer", "klaver aas"]
    ruiten = ['ruiten 2', 'ruiten 3', 'ruiten 4', 'ruiten 5', 'ruiten 6', 'ruiten 7', 'ruiten 8', 'ruiten 9', 'ruiten 10', " ruiten boer", "ruiten vrouw", "ruiten heer", "ruiten aas"]
    joker = ['joker', 'joker']
    cards = harten+schoppen+klaver+ruiten+joker
    nummer = 0
    random.shuffle(cards)
    for i in range(7):
        hand = []
        hand.append(cards.pop(random.randint(0, 5)))
        nummer += 1
        print("kaart", nummer, ':', hand)
    print('deck [47 kaarten] ', cards)

kaartspel()