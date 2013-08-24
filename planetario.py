import  pygame
from color import *
import random
#from cinematic import *

#pygame.display.Info()

size = width, height = 1920 , 1080

def no_force(screen):# no force.
            g = 0
            #a point
            x = random.randint(0,width)
            y = random.randint(0,height)
            astro(screen,x,y,0)
            
def lateral_force(screen,t):# lateral force.
            g = -9.81
            x_0 =  width/2-300
            y_0 =  height/2
            v_0x = 30
            v_0y = 45
            x = x_0
            y = y_0
            lateral = 1
            x_old=x
            y_old=y
            x =                x_0 + v_0x * t 
            y = height -(y_0 + v_0y * t + 1./2. * g * t * t)
            if y > height :
                t = 0
            if x > width :
                t = 0
            astro(screen,x,y,1) 
                            
                          
def centripete_force(screen,t):
            pass
            #planeta.x= x_0 + v_x * t + 1/2 * g_x *t*t
            #planeta.y = y_0 + v_y *t +1/2 * g_y *t*t
def centrifuge_force(screen,t):# central force, centrifuga.
            pass

def astro(screen,x,y,astro):
    if astro == 0:
        pygame.draw.circle(screen, white,[int(x),int(y)] , 5, 0)
    else:
        pygame.draw.circle(screen,red,[int(x),int(y)],5,0)
        #image.load('planeta.tga')
        #mejorar con planeta.box(              
