from datetime import datetime
from tkinter import Tk, Canvas
import pygame
pygame.init()
date = datetime.now()
window = Tk()
window.title("Connie's Calender")
c = Canvas(window, width=800, height=700, bg="light blue")
c.pack()
#heading
c.create_text(100,50, anchor="w", fill="green",\
font="Arial 28 bold underline", text="Connie's Calender")
#date text
c.create_text(100,100, anchor="w", fill="green",\
font="Arial 28", text=date)
#sound track
music = pygame.mixer.Sound("sounds/Raining Tacos.wav")
music.play()
#frt6r5
