print("WELCOME TO RPG SURVIVAL")
print("INSTRUCTIONS:")
print("Go (Direction)")
print("Do (thing)")
print("Show inventory")
inventory = ["Axe"]
print("INVENTORY:", inventory)
tsk1 = input("You are in a dark forest surrounded by trees what do you do?")
if (tsk1 == "Do cut trees") :
  print("You swung your axe high and gained 20 wood")
  inventory.append("Wood")
  tsk2 = input("Its Lunch time and your getting hungry! What do you do?")
else if(tsk1 == "Go north" or tsk1 == "Go North") :
  tsk3 = input("You went north and found a inn what do you do?")
  if (tsk3 == "Do enter inn" or tsk3 == "Do go in inn") :
    if ("Wood" not in inventory) :
      print("INNKEEPER: You can only rest at my inn if you give me wood from the trees")
else if (tsk2 == "Show inventory") :
    print(inventory)

  
