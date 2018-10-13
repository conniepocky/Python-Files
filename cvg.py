from tkinter import Tk
from tkinter import *
#vars
window = Tk()
window.title("CvT Gaming")
c = Canvas(window, width=900, height=500)
meh = Label(window, text="CvT Games", font='size, 40', fg="orange")
meh.pack()
#functions
def ms():
    import ms
def exit():
    window.destroy()
    quit()
#games
bquit = Button(window, text="Quit", command=exit)
bquit.pack()
met = Button(window, text="Meteor Shower", command=ms)
met.pack() 
#run
c.pack()
window.mainloop()
