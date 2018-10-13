#imports
import pygame
from time import sleep
import sys
pygame.init()

#colours
WHITE = (255,255,255)
BLACK = (0,0,0)
GREEN = (0,255,127)
#functions
def char(x,y):
    window.blit(cherry, (x,y))
def text_objects(text, font):
    textSurface = font.render(text, True, BLACK)
    return textSurface, textSurface.get_rect()

def message_display(text):
    largeText = pygame.font.Font('freesansbold.ttf',50)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((windoww/2),(windowh/2))
    window.blit(TextSurf, TextRect)

    pygame.display.update()
#Set caption
pygame.display.set_caption("Sky Islands")
icon = pygame.image.load("sword.png")
pygame.display.set_icon(icon)
#Game loop
def game():
    #vars
    windoww = 800
    windowh = 600
    window = pygame.display.set_mode((windoww,windowh))
    alive = True
    clock = pygame.time.Clock()
    #vars
    x = (windoww * 0.8)
    y = (windowh * 0.8)
    xm = 0
    cherry = pygame.image.load("pcherry.png")
    while alive:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
               alive == False
               pygame.quit()
               sys.exit()
               quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    xm = -5
                elif event.key == pygame.K_RIGHT:
                    xm = 5
        
         window.fill(GREEN)
         char(x,y)
         pygame.display.update()
         clock.tick(60)
#intro
def intro():
    window.fill(WHITE)
    message_display("Sky Islands")
    sleep(2)
    game()
#run
intro()
    
