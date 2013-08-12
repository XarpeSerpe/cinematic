# TO DO
#recalibrar ejes para que quepa el movimiento 
#dibujar numeros en los ejes
#revisar la exponienciacion **?

import sys, pygame, math, random
pygame.init()
size = width, height = 800 , 450

x_0 = 0
y_0 = 0
v_0x = 35
v_0y = 75
g =  -10

t_max = ( v_0y + ( v_0y ** 2 + 2 * g * y_0 ) ** 0.5 ) / g
y_max = y_0 + v_0y * t_max - 1 / 2 * g * t_max
x_max = x_0 + v_0x * t_max
 
screen = pygame.display.set_mode(size, pygame.FULLSCREEN)
screen.fill([255,255,255])
color = 0, 200, 0
white = 255,255,255
mainloop, color, fontsize, delta, fps =  True,  (32,32,32), 35, 1, 30
x, y = 0, 0
t = 0
Clock = pygame.time.Clock()
 
while mainloop:
    tickFPS = Clock.tick(fps)
    pygame.draw.circle(screen, white,[x,y] , 25, 5)
    #fontsize = random.randint(35, 150)
    #myFont = pygame.font.SysFont("None", fontsize)
    #color = (random.randint(0,255), random.randint(0,255), random.randint(0,255))
    screen.fill((255,255,255))
    #screen.blit(myFont.render("I love pygame!", 0, (color)), (x,y))
    #start_pos = random.randint(0,800),random.randint(0,800)
    #end_pos = random.randint(0,450),random.randint(0,450)
    #pygame.draw.line(screen, color, start_pos, end_pos, 10) 
    pygame.draw.line(screen, color, [0, height/2], [width, height/2], 1)
    pygame.draw.line(screen, color, [width/2, 0], [width/2, height], 1)
    for x in range(width/10) :
        pygame.draw.line(screen, color,[0+x*10, height/2+3], [0+x*10, height/2-3],1)
    for y in range(height/10) :
        pygame.draw.line(screen, color,[width/2+3,0+y*10], [width/2-3,0+y*10 ],1)
     
    t = t +1 
    x = x_0 + v_0x * t
    y = height -(y_0+v_0y*t+g/2*t**2)
    
    if y > height :
        t = 0
    if x > width :
        t = 0
    pygame.draw.circle(screen, color,[x,y] , 25, 5)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            mainloop = False # Be IDLE friendly!
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                mainloop = False # Be IDLE friendly!
    pygame.display.update()
 
pygame.quit() # Be IDLE friendly! 
