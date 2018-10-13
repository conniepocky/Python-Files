#imports
import pygame
pygame.init()
#vars
window = pygame.display.set_mode((800,600))
alive = True
clock = pygame.time.Clock()
#Set caption
pygame.display.set_caption("The Quest for the Lightning Rod")
#Game loop
while alive:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print(event)
            alive == False
            pygame.quit()
