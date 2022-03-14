import random

dice = []

one = 0
two = 0
three = 0
four = 0
five = 0
six = 0

ThreeOfaKind = 0
FourOfaKind = 0
FullHouse = 0
SmallStraight = 0
LargeStraight = 0
Yathzee = 0
chance = 0

def scoreboard():
    Total1 = one + two + three + four + five + six
    Total2 = ThreeOfaKind + FourOfaKind + FullHouse + SmallStraight + LargeStraight + Yathzee + chance
    Total = Total1 + Total2
    print(f"""
    scoreboard
    
    one total 1's  score: {one}
    
    two total 2's  score: {two}
    
    three total 3's score: {three}
    
    four total 4's score: {four}
    
    five total 5's score: {five}
    
    six total 6's score: {six}

    extra bonus if sore is 63 or more +35 points

    total part1 score: {Total1}





    three of a kind total dice score: {ThreeOfaKind}

    four of a kind total dice  score: {FourOfaKind}

    full house 25 points score: {FullHouse}

    small straight 30 point score: {SmallStraight}

    large straight 40 point score: {LargeStraight}

    yathzee 50 points score: {Yathzee}

    chance  total dice score: {chance}

    total part 2 score: {Total2}

    total part 1 score: {Total1}

    total score   score: {Total}
    """)


def chances():
    global chance
    vraag =  input("wilt u een chance gebruiken? Y/N: ").upper()
    if vraag == "Y":
        chance = sum(dice) 
    else:
        pass

def rollDice():
    for x in range(5):
        dice.append(random.randint(1,6))
    print(dice)

    for i in range(2):
        if chance < 1:
            chances()
            dice.clear()
            rollDice()
        else:
            pass
        throwAgain = input("welke dobbelsteen wilt u opnieuw gooien 1 2 3 4 5. vergeet geen spatie tussen de nummers te zetten.").split()
        print(throwAgain)
        if throwAgain == "stop":
            scoreboard
        elif len(throwAgain) >0:
            for u in throwAgain:
                randomNumber = random.randint(1,6)
                dice[int(i)-1] = randomNumber
        
        print(dice)

def isfullHouse(dice):
    setDice = set(dice)
    diceFullhouse = len(setDice)
    if diceFullhouse == 2:
        if dice.count(dice[0]) == 2 or dice.count(dice[0]) == 3:
            return True
    return False

def Type():
    global one, two, three, four, five, six, ThreeOfaKind, FourOfaKind, FullHouse, SmallStraight, LargeStraight, Yathzee, chance 
    choice = input('onder welke categorie wilt u de punten toevoegen?: ')
    if choice == "one":
        if one >= 1:
            print("sorry u heeft dit al ingevuld.")
            Type()
        else:
            one = (dice.count(1))
    elif choice == "two":
        if two >= 1:
            print("sorry u heeft dit al ingevuld.")
            Type()
        else:
            two = (dice.count(2))*2
    elif choice == "three":
        if three >= 1:
            print("sorry u heeft dit al ingevuld.")
            Type()
        else:
            three = (dice.count(3))*3
    elif choice == "four":
        if four >= 1:
            print("sorry u heeft dit al ingevuld.")
            Type()
        else:
            four = (dice.count(4))*4
    elif choice == "five":
        if five >= 1:
            print("sorry u heeft dit al ingevuld.")
            Type()
        else:
            five = (dice.count(5))*5
    elif choice == "six":
        if six >= 1:
            print("sorry u heeft dit al ingevuld.")
            Type()
        else:
            six = (dice.count(6))*6
    elif choice == "ThreeOfaKind":
        if ThreeOfaKind >= 1:
            print("sorry u heeft dit al ingevuld.")
            Type()
        else:
            if dice.count(1) == 3 or dice.count(2) == 3 or dice.count(3) == 3 or dice.count(4) == 3 or dice.count(5) == 3 or dice.count(6) == 3:
                ThreeOfaKind = sum(dice)
    elif choice == "FourOfaKind":
        if FourOfaKind >= 1:
            print("sorry u heeft dit al ingevuld.")
            Type()
        else:
            if dice.count(1) == 4 or dice.count(2) == 4 or dice.count(3) == 4 or dice.count(4) == 4 or dice.count(5) == 4 or dice.count(6) == 4:
                FourOfaKind = sum(dice)
    elif choice == "FullHouse":
        if FullHouse(dice) >= 1:
            print("sorry u heeft dit al ingevuld.")
            Type()
        else:
            FullHouse = 25
    elif choice == "SmallStraight":
        if SmallStraight >= 1:
            print("sorry u heeft dit al ingevuld.")
            Type()
        else:
            if 1 in dice and 2 in dice and 3 in dice and 4 in dice:
                SmallStraight = 30
            elif 2 in dice and 3 in dice and 4 in dice and 5 in dice:
                SmallStraight = 30
            elif 3 in dice and 4 in dice and 5 in dice and 6 in dice:
                SmallStraight = 30
            else:
                print("u heef geen smallStraight")
            Type()
    elif choice == "LargeStraight":
        if LargeStraight >=1:
            print("sorry u heeft dit al ingevuld.")
            Type()
        else:
            if 1 in dice and 2 in dice and 3 in dice and 4 in dice and 5 in dice:
                LargeStraight = 40
            if 2 in dice and 3 in dice and 4 in dice and 5 in dice and 6 in dice:
                LargeStraight = 40
            else:
                print("soory u heeft geen Large Straight")
                Type()
    elif choice == "Yathzee":
        if Yathzee >= 1:
            print("sorry u heeft dit al ingevuld.")
            Type()
        else:
            if dice.count(dice[0]) == 5:
                Yathzee = 50
            else:
                print("sorry u heeft geen Yahtzee")
                Type()
    else:
        print("sorry dit begrijp ik niet.")
    dice.clear

def board():
    if one != 0 and two != 0 and three != 0 and four != 0 and five != 0 and six != 0:
        return False
    return True

def begin():
    dobbelen = input("druk op enter om de beginnen.")
    if dobbelen == "":
        print(" ")
    elif dobbelen == "stop":
        quit()
    else:
        print("sorry dit begrijp ik niet.")
        begin()
    while board():
        rollDice()
        Type()
    scoreboard()


begin()