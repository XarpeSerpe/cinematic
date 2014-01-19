#Scenes

import sys, math, random, string #falta time?
from math import *
from pygame import *
from dynamics import *
from screen_setup import *
from cinematic import *

from axis import x_axis, y_axis
 
def scene_0 ():
    screen.fill(black)
    fontsize = 50
    #proton masa 1800 la del electron 
    x =width/2
    y = height/2
    pos = [x, y]
    pygame.draw.circle(screen, red, pos, 20)
    myFont = pygame.font.SysFont("None", fontsize)
    screen.blit(myFont.render("Proton", 0, (red)), (x-60,y-60))
    pygame.display.update()
    #time.delay(2000)
    screen.blit(myFont.render("Neutron",0,(black)),(x-40,y-50))
    x+=7
    y+=8
    pos=[x,y]
    pygame.draw.circle(screen, black, pos,21,21)
    pygame.display.update()
    #time.delay(2000)
   
    while 1:
        
        #autofuncion_un_electron(Z,n,l,m)
        autofuncion_un_electron (1, 1, 0, 0,1000)
        autofuncion_un_electron (1, 2, 0, 0,1000)
        autofuncion_un_electron (1, 2, 1, 0,1000)
        #orbital P

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
    
def scene_3 ( ):
    pass
    
def scene_4():
    screen.fill(black)
    fontsize = (50)
    myFont = pygame.font.SysFont("None", fontsize)
    screen.blit(myFont.render("Give me V_x", 0, (red)), (x,y))
    print ask(screen, "Name") + " was entered"
    pygame.display.update()
   
def get_key():
       while 1:
           event = pygame.event.poll()
           if event.type == pygame.KEYDOWN:
            return event.key
       else:
           pass

def display_box(screen, message):
  "Print a message in a box in the middle of the screen"
  fontobject = pygame.font.Font(None,18)
  pygame.draw.rect(screen, (0,0,0),
                   ((screen.get_width() / 2) - 100,
                    (screen.get_height() / 2) - 10,
                    200,20), 0)
  pygame.draw.rect(screen, (255,255,255),
                   ((screen.get_width() / 2) - 102,
                    (screen.get_height() / 2) - 12,
                    204,24), 1)
  if len(message) != 0:
    screen.blit(fontobject.render(message, 1, (255,255,255)),
                ((screen.get_width() / 2) - 100, (screen.get_height() / 2) - 10))
  pygame.display.flip()

def ask(screen, question):
  "ask(screen, question) -> answer"
  pygame.font.init()
  current_string = []
  display_box(screen, question + ": " + string.join(current_string,""))
  while 1:
    inkey = get_key()
    if inkey == pygame.K_BACKSPACE:
      current_string = current_string[0:-1]
    elif inkey == pygame.K_RETURN:
      break
    elif inkey == pygame.K_MINUS:
      current_string.append("_")
    elif inkey <= 127:
      current_string.append(chr(inkey))
    display_box(screen, question + ": " + string.join(current_string,""))
  return string.join(current_string,"")
