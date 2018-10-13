#QUICK REACTION GAME
#Imports
import time
import pygame
#Init
pygame.init()
#Vars
gameDisplay = pygame.display.set_mode((800,700))

music = pygame.mixer.Sound("mamma mia.wav")
#Print
while True:
    print("Starting new round...")
    time.sleep(5)
    music.play()
    print("---------------------------")
pygame.quit()
