from tkinter import *
from tkinter import messagebox
from random import choice
window = Tk()
houses = ["Gryffindor","Hufflepuff","Ravenclaw","Slytherin"]
c = Canvas(window, height=300, width=400, bg="brown")
c.pack()
def pickhouse(event):
    messagebox.showinfo("Sorting Hat", choice(houses))
c.bind_all("<Button-1>", pickhouse)

    
    
