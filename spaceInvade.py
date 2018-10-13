import pygame, sys
from pygame.locals import *
pygame.mixer.init()
pygame.init()
DISPLAYSURF = pygame.display.set_mode((400, 300))
pygame.display.set_caption('Space invaders')
music = pygame.mixer.Sound("sounds/Raining Tacos.wav")
music.play()
# Data
alienX = 200
alienY = 20
alienDir = 0
shipX = 200
shipY = 280
laserX = 0
laserY = 0

# set up the colours
BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
RED   = (255,   0,   0)
GREEN = (  0, 255,   0)
BLUE  = (  0,   0, 255)

def drawScreen():
    DISPLAYSURF.fill(BLACK)
    drawAlien()
    drawShip()
    drawLaser()
    pygame.display.update()
    return


def drawAlien():
    x = alienX
    y = alienY
    points = [(x,y+10),(x-10,y-10),(x+10,y-10)]
    pygame.draw.lines(DISPLAYSURF,RED,True,points,1)
    return

def drawLaser():
    global laserX, laserY
    if laserY >= 1 :
        points = [(laserX,laserY+10),(laserX,laserY)]
        pygame.draw.lines(DISPLAYSURF,WHITE,False,points,1)
    return

def drawShip():
    x = shipX
    y = shipY
    points = [(x,y-10),(x-10,y+10),(x+10,y+10)]
    pygame.draw.lines(DISPLAYSURF,GREEN,True,points,1)
    return

def moveAlien():
    global alienDir, alienX, alienY
    if alienDir == 0:
        alienX = alienX - 1
        if alienX == 0:
            alienDir = 1
    if alienDir == 1:
        alienX = alienX + 1
        if alienX == 400:
            alienDir = 0
    return

def moveLaser():
    global laserY
    if laserY >=1 :
        laserY = laserY - 5
    return

def fireLaser():
    global laserY,laserX
    if laserY <= 0 :
        laserY = shipY
        laserX = shipX
    return

def checkLaser():
    global laserX,laserY,alienX,alienY
    if (laserX > alienX-10 and laserX < alienX+10
        and laserY > alienY-10 and laserY < alienY+10) :
        alienY = -20
    return

def checkKeys():
    global shipX, shipY
    if pygame.key.get_pressed()[pygame.K_LEFT] !=0 :
        shipX = shipX - 3
    if pygame.key.get_pressed()[pygame.K_RIGHT] !=0 :
        shipX += 3
    if pygame.key.get_pressed()[pygame.K_SPACE] !=0 :
        fireLaser()
    return




gameclock = pygame.time.Clock()
while True: # main game loop

    # Restrict the speed of the movement
    gameclock.tick(30)
    
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    # Move the alien
    moveAlien()

    # Move the laser
    moveLaser()
        
    # Draw the screen
    drawScreen()

    # Check keyboard input
    checkKeys()
    
    # Check laser collision
    checkLaser()
