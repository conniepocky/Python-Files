import pygame, time
pygame.init()
window = pygame.display.set_mode((800,600))
pygame.display.set_caption("Happy - Sad")
clock = pygame.time.Clock()
happy = pygame.image.load("happy.png")
sad = pygame.image.load("sad.png")
white = (255,255,255)
def happy(x,y):
    window.blit(happy,(x,y))
def sad(sx,sy):
    pass
hx = (800*0.45)
hy = (600*0.8)
Running = True
while Running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            Running = False
    window.fill(white)
    happy(hx,hy)
    pygame.display.update()
    clock.tick(60)
pygame.quit()
