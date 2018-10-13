import pygame
pygame.init()
#vars
playing = True
layerOn = 0
window = pygame.display.set_mode((50,50))
people = ["Margaret", "Ian", "Leila", "Sharon", "Richard", "Natalia"]
print('''                         Names
''' , people ,'''
                        Layers
5/10/15/20/25/30''')
print("Press space when the music stops!")
while playing:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                layerOn += 1
                print("You are on layer ", layerOn)
                
