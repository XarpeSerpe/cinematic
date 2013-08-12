# TO DO
#recalibrar ejes para que quepa el movimiento 
#dibujar numeros en los ejes


import sys, pygame, math, random
from color import *
from cinematic import *
from axis import x_axis, y_axis

pygame.init()
size = width, height = 800 , 450

screen = pygame.display.set_mode(size,pygame.FULLSCREEN)
screen.fill(black)

mainloop =  True
Clock = pygame.time.Clock()

x_axis(screen)
y_axis(screen)

while mainloop:
    tickFPS = Clock.tick(35)
    #pygame.display.set_caption("Press Esc to quit. FPS: %.2f" % (Clock.get_fps()))
    #pygame.draw.circle(screen, black,[int(x),int(y)] , 5, 5)
    #fontsize = random.randint(35, 150)
    #myFont = pygame.font.SysFont("None", fontsize)
    #color = (random.randint(0,255), random.randint(0,255), random.randint(0,255))
    #screen.fill(black)
    #screen.blit(myFont.render("I love pygame!", 0, (color)), (x,y))
    #start_pos = random.randint(0,800),random.randint(0,800)
    #end_pos = random.randint(0,450),random.randint(0,450)
    #
    

  
    t = t +0.1
    x_old=x
    y_old=y
    x = x_0 + v_0x * t
    y = height -(y_0+v_0y*t+g/2*t**2)
    
    if y > height :
        t = 0
    if x > width :
        t = 0
    #pygame.draw.circle(screen, blue,[int(x),int(y)] , 5, 5)
    pygame.draw.line(screen, red, [x_old, y_old], [x,y], 1) 
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            mainloop = False # Be IDLE friendly!
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                mainloop = False # Be IDLE friendly!
    pygame.display.update()
 
pygame.quit() # Be IDLE friendly! 
