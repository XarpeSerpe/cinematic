#Scenes

import sys, math, random, pygame, time
from dynamics import *
from screen_setup import *
from cinematic import *
from axis import x_axis, y_axis


def scene_1():
    #draw reference sistem 
    x_axis(screen)
    y_axis(screen)
    fontsize = 50
    myFont = pygame.font.SysFont("None", fontsize)
    screen.blit(myFont.render("Random dots, no forces", 0, (red)), (x,y))
    no_force(screen)
    pygame.display.update()

def scene_2():
    screen.fill(black)
    x_axis(screen)
    y_axis(screen)
    fontsize = 50
    myFont = pygame.font.SysFont("None", fontsize)
    
    screen.blit(myFont.render("Parabolic Throw", 0, (red)), (x,y))
        
    for t in range (10):
        lateral_force(screen,t)
        time.sleep(1)
        pygame.display.update()
    

def scene_3():
    screen.fill(black)
    
    fontsize = random.randint(35, 150)
    myFont = pygame.font.SysFont("None", fontsize)
    
    #screen.fill(black)
    screen.blit(myFont.render("Scene 3", 0, (red)), (x,y))
    pygame.display.update()
