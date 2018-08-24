import pygame
import numpy as np
import time

pygame.init()

resx = 640
resy = 480

screen = pygame.display.set_mode((resx,resy))  # Set resolution for monitor 1440x1200 or w/e
xoff = int(resx/2)
yoff = int(resy/2)

pygame.draw.circle(screen,(255,255,0),(xoff,yoff),10)
pygame.display.update()
time.sleep(3)
print('Start behaviour')

N_rep = 20

for i in range(N_rep): 

   pygame.draw.circle(screen,(255,255,0),(xoff,yoff),10)
   pygame.display.update()
   time.sleep(3)
   sel = np.random.randint(1,9)
   
   if sel == 1:
        pygame.draw.circle(screen,(0,0,0),(xoff,yoff),10)
        pygame.draw.circle(screen,(255,0,0),(0+xoff,100+yoff),10)
        pygame.display.update()
        time.sleep(1.4)
        pygame.draw.circle(screen,(0,0,0),(0+xoff,100+yoff),10)
        pygame.display.update()
   
   if sel == 2:
        pygame.draw.circle(screen,(0,0,0),(xoff,yoff),10)
        pygame.draw.circle(screen,(255,0,0),(100+xoff,0+yoff),10)
        pygame.display.update()
        time.sleep(1.4)
        pygame.draw.circle(screen,(0,0,0),(100+xoff,0+yoff),10)
        pygame.display.update()
   
   if sel == 3:
        pygame.draw.circle(screen,(0,0,0),(xoff,yoff),10)
        pygame.display.update()
        pygame.draw.circle(screen,(255,0,0),(-100+xoff,0+yoff),10)
        pygame.display.update()
        time.sleep(1.4)
        pygame.draw.circle(screen,(0,0,0),(-100+xoff,0+yoff),10)
        pygame.display.update()

   if sel == 4:
        pygame.draw.circle(screen,(0,0,0),(xoff,yoff),10)
        pygame.display.update()
        pygame.draw.circle(screen,(255,0,0),(0+xoff,-100+yoff),10)
        pygame.display.update()
        time.sleep(1.4)
        pygame.draw.circle(screen,(0,0,0),(0+xoff,-100+yoff),10)
        pygame.display.update()

   if sel == 5:
        pygame.draw.circle(screen,(0,0,0),(xoff,yoff),10)
        pygame.display.update()
        pygame.draw.circle(screen,(255,0,0),(-71+xoff,-71+yoff),10)
        pygame.display.update()
        time.sleep(1.4)
        pygame.draw.circle(screen,(0,0,0),(-71+xoff,-71+yoff),10)
        pygame.display.update()

   if sel == 6:
        pygame.draw.circle(screen,(0,0,0),(xoff,yoff),10)
        pygame.display.update()
        pygame.draw.circle(screen,(255,0,0),(xoff+71,-71+yoff),10)
        pygame.display.update()
        time.sleep(1.4)
        pygame.draw.circle(screen,(0,0,0),(xoff+71,-71+yoff),10)
        pygame.display.update()

   if sel == 7:
        pygame.draw.circle(screen,(0,0,0),(xoff,yoff),10)
        pygame.display.update()
        pygame.draw.circle(screen,(255,0,0),(-71+xoff,yoff+71),10)
        pygame.display.update()
        time.sleep(1.4)
        pygame.draw.circle(screen,(0,0,0),(-71+xoff,yoff+71),10)
        pygame.display.update()

   if sel == 8:
        pygame.draw.circle(screen,(0,0,0),(xoff,yoff),10)
        pygame.display.update()
        pygame.draw.circle(screen,(255,0,0),(xoff+71,yoff+71),10)
        pygame.display.update()
        time.sleep(1.4)
        pygame.draw.circle(screen,(0,0,0),(xoff+71,yoff+71),10)
        pygame.display.update()

