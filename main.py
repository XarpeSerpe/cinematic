# TO DO
#comenzar a trabajar por capas
#recalibrar ejes para que quepa el movimiento 
#dibujar numeros en los ejes
#Anhadir vectores

import sys, math, random, pygame
from dynamics import *
from screen_setup import *

from axis import x_axis, y_axis
from scenes import *

pygame.init()
               
screen = pygame.display.set_mode(size)#,pygame.FULLSCREEN)
screen.fill(black)

mainloop =  True

Clock = pygame.time.Clock()

while mainloop:
    
    #scene_0()
    scene_1()
    #scene_2() falla
    #scene_3()
    #scene_4() falla
    scene_5()
    #scene_6() no existe
    #scene_7() no existe
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                mainloop = False # Be IDLE friendly!
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    mainloop = False # Be IDLE friendly!    pygame.display.update()
  
pygame.display.quit()
pygame.quit() # Be IDLE friendly! 

