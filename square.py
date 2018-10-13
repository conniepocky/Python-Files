from tkinter import *
import time
tk = Tk()
tk.title("Squarey")
c = colorchooser.askcolor(title='Choose Squarey\'s Color')
canvas = Canvas(tk, width=700, height=700)
canvas.pack()
class Squarey:
    def __init__(self, canvas, color):
        self.canvas = canvas
        self.id = canvas.create_rectangle(10, 10, 50, 50, fill=color)
    def draw(self, pos):
        def move(event):
            if event.keysym == 'Up':
                self.canvas.move(self.id, 0, -5)
            elif event.keysym == 'Down':
                self.canvas.move(self.id, 0, 5)
            elif event.keysym == 'Left':
                self.canvas.move(self.id, -5, 0)
            else:
                self.canvas.move(self.id, 5, 0)
        canvas.bind_all('<KeyPress-Up>', move)
        canvas.bind_all('<KeyPress-Down>', move)
        canvas.bind_all('<KeyPress-Left>', move)
        canvas.bind_all('<KeyPress-Right>', move)
class Tele:
    def __init__(self, canvas, pos):
        self.canvas = canvas
        self.id = canvas.create_text(10, 10, text=pos)
    def draw(self, pos):
        canvas.delete(self.id)
        self.id = canvas.create_text(350, 350, text=pos)
squarey = Squarey(canvas, c[1])
pos = squarey.canvas.coords(squarey.id)
tele = Tele(canvas, pos)
while 1:
    pos = squarey.canvas.coords(squarey.id)
    squarey.draw(pos)
    tele.draw(pos)
    tk.update_idletasks()
    tk.update()
    time.sleep(0.01)
