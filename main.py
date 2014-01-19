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

i = 0

while mainloop:
    i = i + 1 
    if i < 2000 :
        scene_0()
    if i < 2500 and i >= 2000:
        scene_1()
    elif i == 2500:
        scene_2()
    else:
        scene_4()
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                mainloop = False # Be IDLE friendly!
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    mainloop = False # Be IDLE friendly!    pygame.display.update()
  

pygame.display.quit()
pygame.quit() # Be IDLE friendly! 
v
