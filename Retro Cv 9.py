#Retro Cv 9
import random
import webbrowser
funActivities = ["Play Roblox with friends.", "Video call friends", "Play video games", "Program", "Read Harry Potter"]
while True:
    command = input(">")
    if command == "bored":
        print(random.choice(funActivities))
    elif command == "asignInt":
        name = input("NAME INPUT REQUIRED")
        print(name , ":" , random.randint(1, 9999))
    elif command == "games":
        print("""
KOTD
SPACE_INVADE
""")
    elif command == "KOTD":
        webbrowser.open("http://technovisualeducation.co.uk/webspace/connie/adventure/index.html")
    elif command == "SPACE_INVADE":
        import spaceInvade
        
    else:
        print(command)
