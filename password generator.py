import random

choicesLC = [random.choice("abcdefghijklmnopqrstuvwxyz") for i in range(2)]
choicesUP = [random.choice("ABCDEFGHIJKLMNOPQRSTUVWXYZ")for i in range(random.randint(1, 3))]
choicesNUM = [random.choice("123456789")for i in range(random.randint(4,7))]
chocieSYM =  [random.choice("!@#$%^&*()")for i in range(3)]

choices_LW_UP = choicesLC + choicesUP
random.shuffle(choices_LW_UP)
choiceALL = choicesLC+choicesUP+choicesNUM+chocieSYM
random.shuffle(choiceALL)
choiceTotall = choices_LW_UP + choiceALL
choiceSUM = 24-len(choiceTotall)
choiceADD = [random.choice("abcdefghijklmnopqrstuvwxyz") for y in range(choiceSUM)]
if len(choiceTotall) < 24:
    print("".join( choiceTotall+choiceADD))
else:
    print(choiceTotall)