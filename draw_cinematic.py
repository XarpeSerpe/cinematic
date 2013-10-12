# TO DO
#comenzar a trabajar por capas
#recalibrar ejes para que quepa el movimiento 
#dibujar numeros en los ejes
#Anhadir vectores


import sys, math, random, pygame
from force import *
from color import *
from cinematic import *
from axis import x_axis, y_axis

pygame.init()
size = width, height = 800 , 600


def espera ( ):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            mainloop = False # Be IDLE friendly!
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                mainloop = False # Be IDLE friendly!
                
screen = pygame.display.set_mode(size)#,pygame.FULLSCREEN)
screen.fill(black)

mainloop =  True

Clock = pygame.time.Clock()

t = 0
while mainloop:
    
     
    #draw reference sistem 
    x_axis(screen)
    y_axis(screen)
    
    tickFPS = Clock.tick(35)
    #pygame.display.set_caption("Press Esc to quit. FPS: %.2f" % (Clock.get_fps()))
    #
    #fontsize = random.randint(35, 150)
    #myFont = pygame.font.SysFont("None", fontsize)
    #color = (random.randint(0,255), random.randint(0,255), random.randint(0,255))
    #screen.fill(black)
    #screen.blit(myFont.render("I love pygame!", 0, (color)), (x,y))
    #trayectoria pygame.draw.line(screen, red, [x_old, y_old], [x,y], 1) 
    # Coordenadas:
    #Clean axis
    #pygame.draw.line(screen, black, [width/2, y], [x,y], 1) 
    #pygame.draw.line(screen, black, [x, height/2], [x,y], 1)  
    #pygame.draw.line(screen, blue, [width/2, y], [x,y], 1) 
    #pygame.draw.line(screen, blue, [x, height/2], [x,y], 1)  
    
    #no_force(screen)
    lateral_force(screen,t)
    pygame.display.update()
    t = t + 1
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                mainloop = False # Be IDLE friendly!
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    mainloop = False # Be IDLE friendly!    pygame.display.update()
  

pygame.display.quit()
pygame.quit() # Be IDLE friendly! 
