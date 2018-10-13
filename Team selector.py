from random import choice
players = ["Dumbledore", "Voldy whos gone Mouldy", "Snape", "Harry"]
teamA = []
teamB = []
while len(players) > 0:
    playerA = choice(players)
    teamA.append(playerA)
    players.remove(playerA)
    playerB = choice(players)
    teamB.append(playerB)
    players.remove(playerB)

print("Team A is ", teamA)
print("Team B is ", teamB)
    
   
    
