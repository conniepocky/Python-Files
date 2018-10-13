#Imports
from tkinter import *
from tkinter import Tk
#Vars
window = Tk()
screen = Canvas(window, width=1000, height=1000)
points1 = 0
points2 = 0
window.title("Spammer Pro!")
#Create Shapes and Labels
title = Label(window, text="Spammer Pro!", font='size, 40', fg="purple")
instructions = Label(window, text="Player 1 Press Q and Player 2 press M to gain points!!", fg="blue")
playerOnePoints = Label(window, text=points1,bg="red", fg="blue")
#Functions
def keyTracker(event):
    if event.keysym == "KeyPress-q":
        points1 += 1
        print(1)
        playerOnePoints.config(text=points1, width=100)
    if event.keysym == "KeyPress-m":
        points2 += 1
        

#Run 
screen.bind_all("<Key>", keyTracker)
playerOnePoints.pack(fill=X)
instructions.pack()
title.pack()
screen.pack()
window.mainloop()
