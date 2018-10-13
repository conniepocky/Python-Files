from random import randint
# selections
player = input("Type your choice, (rock) (paper) (sciccors)")
comChoice = randint(1,3)

if (comChoice == 1):
    computer = "rock"
if (comChoice == 2):
    computer = "paper"
if (comChoice == 3):
    computer = "sciccors"
#result
print(player, "vs", computer) 

