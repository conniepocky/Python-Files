#CvT 2017 All rights reserved.
#Imports
import webbrowser
import pygame
from tkinter import *
from tkinter import messagebox
from tkinter.messagebox import showinfo
from tkinter.simpledialog import askstring
from datetime import datetime
from random import randint
pygame.init()
#vars
window = Tk()
c = Canvas(window, width=800, height=600)
window.title("CvT OS")
date = datetime.now()
title = Label(window, text="Cvt OS", bg="green", fg="black")
title.pack(fill=X)
dateLabel = Label(window, text=date, fg="black")
dateLabel.pack(side=BOTTOM)
#functions
def quit():
    window.destroy()
    music.stop()
    piano.stop()
def notes():
    note = askstring("CvT", "Type your note in the area below.")
    noteLabel = Label(window, text=note, bg="red", fg="orange")
    noteLabel.pack(fill=X)
def bing():
    webbrowser.open("https://www.bing.com/")
def about():
    showinfo("CvT", "This is OS 1.0")
def songplaylist():
    showinfo("CvT", "Here are your songs which you can type into  CvT sounds and they will magicly play.")
    showinfo("CvT", "1: Nyan Cat")
    showinfo("CvT", "2: Piano")
#menu vars
menu = Menu(window)
window.config(menu=menu)
subMenu = Menu(menu)
subMenu1 = Menu(menu)

#menus
menu.add_cascade(label="System", menu=subMenu)
subMenu.add_command(label="Exit", command=quit)
subMenu.add_command(label="About", command=about)
subMenu.add_command(label="Songs", command=songplaylist)
menu.add_cascade(label="Applications", menu=subMenu1)
subMenu1.add_command(label="CvT Notes", command=notes)
subMenu1.add_command(label="Bing", command=bing)
#run
c.pack()
window.mainloop()
