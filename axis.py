import pygame
size = width, height = 800 , 450
green = 0,255,0
x=0
y=0

def x_axis(screen):
    pygame.draw.line(screen, green, [0, height/2], [width, height/2], 1)
    for x in range(width/10) :
        pygame.draw.line(screen, green,[0+x*10, height/2+3], [0+x*10, height/2-3],1)
    
def y_axis(screen):
    pygame.draw.line(screen, green, [width/2, 0], [width/2, height], 1)
    for y in range(height/10) :
        pygame.draw.line(screen, green,[width/2+3,0+y*10], [width/2-3,0+y*10 ],1)
     
