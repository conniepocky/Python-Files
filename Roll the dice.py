from tkinter import *
from tkinter import messagebox
from random import choice
choose = ["1","2","3","4","5","6"]
def roll():
    messagebox.showinfo("Dice", choice(choose))
window = Tk()
button = Button(window, text="Press to roll!", command=roll)
button.pack()
    
