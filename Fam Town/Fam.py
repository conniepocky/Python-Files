#Fam Town
import pygame
import time
pygame.init()
#Vars
w = 800
h = 600
clock = pygame.time.Clock()
brick = pygame.image.load("b.png")
music = pygame.mixer.Sound("n.wav")
pink = (255, 192,203)
green = (0,255,0)
brown = (210,180,140)
blue = (0,0,255)
red = (255,0,0)
yellow = (255,255,0)
grey = (114, 153, 89)
q = False
window = pygame.display.set_mode((w,h))
pygame.display.set_caption("Fam Town")
#functions
def update():
    pygame.display.update()
def makeSprite(color, x, y):
    window.blit(brick, (x,y))
    update()

def text_objects(text, font, c):
    textSurface = font.render(text, True, c)
    return textSurface, textSurface.get_rect()

def message(t, c):
    largeText = pygame.font.Font('freesansbold.ttf',50)
    TextSurf, TextRect = text_objects(t, largeText, c)
    TextRect.center = ((400),(100))
    window.blit(TextSurf, TextRect)

    pygame.display.update()
    time.sleep(2)
 
def showText(text, color):
    message(text, color)
#Game loop
pygame.mixer.Sound.play(music)
while not q:
    x = 400
    mood = "Fine"
    y = 300
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        if event.type == pygame.MOUSEMOTION:
            showText("Mood: Playful!", pink)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                showText("Mood: Happy", green)
            if event.key == pygame.K_z:
                showText("Mood: Very Sad", red)
            if event.key == pygame.K_k:
                showText("Mood: Anxious", grey)
            if event.key == pygame.K_p:
                showText("Mood: ENERGETIC", yellow)
    window.fill(blue)
    makeSprite(brown, x, y)
    update()
    clock.tick(60)
