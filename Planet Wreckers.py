import pygame, sys, time
from pygame.locals import *
import random
pygame.init()
window = pygame.display.set_mode((800,600))
pygame.display.set_caption("Meteor Shower")
music = pygame.mixer.Sound("sounds/sounds/Keyboard.wav")
music.play()
#Colors
GREEN = (0,255,0)
BLACK = (0,0,0)
GREY = (128,128,128)
#vars
ship = pygame.image.load("ship.png")
clock = pygame.time.Clock()
sx = 0
ship_width = 73
#starting coords
x = (800 * 0.45)
y = (600 * 0.8)
def crash():
    message_display("GAME OVER")
def text_objects(text, font):
    textDisplay = font.render(text, True, GREEN)
    return textDisplay, textDisplay.get_rect()
def message_display(text):
    largeText = pygame.font.Font("freesansbold.ttf",115)
    TextDis , TextRect = text_objects(text, largeText)
    TextRect.center = ((800/2),(600/2))
    window.blit(TextDis, TextRect)
    pygame.display.update()
    time.sleep(2)
def things(thingx, thingy, thingw, thingh,color):
    pygame.draw.rect(window, color, [thingx, thingy,thingw,thingh])
def addImg(x,y):
    window.blit(ship, (x,y))
thing_startx = random.randrange(0, 800)
while True:
    #game loop
    thing_starty = 0
    thing_speed = 7
    thing_w = 100
    thing_h = 100
    x += sx
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                sx = -5
            elif event.key == pygame.K_RIGHT:
                sx = 5
        clock.tick(60)
        x += sx
        pygame.display.update()
        window.fill(BLACK)
        #create thing (meteor)
        #things(thingx, thingy, thingw, thingh,color)
        things(thing_startx,thing_starty, thing_w, thing_h, GREY)
        thing_starty += thing_speed
        addImg(x,y)
        if thing_starty > 800:
          thing_starty = 0 - thing_h
          thing_startx = random.randrange(0, 800)
        if y < thing_starty+thing_h:
            if x > thing_startx and x < thing_startx + thing_w or x+ship_width > thing_startx and x + ship_width < thing_startx+thing_w:
                crash()  






        
    

    
                
