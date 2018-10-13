#imports
import pygame
from pygame.ocals import *
from OpenGL.GL import *
from OpenGL.GLU import *
#12 conections
#8 vertices     _
#faces = sides |_| thats a face :)
#vars
vertices = ((-1,-1,-1), (1,1,-1), (-1,1,-1), (-1,-1,-1) , (1,-1,1), (1,1,1), (-1,-1,1), (-1,-1,1))

edges = ((0,1), (0,3), (0,4), (2,1)(2,3), (2,7), (6,3), (6,4), (6,7), (5,1), (5,4), (5,7))

def makeCube():
    glBegin(GL_LINES)
    for edge in edges:
        for vert in edges:
            glVertex3fv(vertices[vertex])
    glEnd()
def main():
    pygame.init()
    window = (800,600)
    pygame.display.set_mode(window, DOUBLEBUF|OPENGL)

    gluPerspectie(45, (window[0]/window[1], 0.1, 50,0)
    glTranslated(0.0,0.0, -5)
    glRotatef(0,0,0,0)
    while True:
            for event in pygame.event.get():
                  if event.type == pygame.QUIT:
                  pygame.quit()
                  quit()
            glclear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
            makeCube()
            pygame.display.flip()
            pygame.time.wait(10)


                  
                  

    
