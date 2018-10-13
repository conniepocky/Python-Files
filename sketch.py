from tkinter import *
window = Tk()
window.title("Pixel sketch's")
c = Canvas(window, width=1000, height=500, bg="white")
c.pack()
def draw(event):
    thing = c.create_rectangle(1,1,10,10, fill="black")
    c.move(thing, event.x, event.y)
c.bind_all("<Button-1>", draw)

