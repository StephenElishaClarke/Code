# Communication via serial port with Polaris Spectra Camera
# Ensure that read write permissions are available: sudo chmod 777 /dev/ttyS0
# sys.path.append("~/p3/lib/python3.5/site-packages")

import sys
import serial as ps
import numpy as np
import pygame
import time
import pandas as pd
from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

ser = ps.Serial(port='/dev/ttyS0',baudrate=115200,bytesize=ps.EIGHTBITS,parity=ps.PARITY_NONE,stopbits = ps.STOPBITS_ONE,timeout=0.2,rtscts=True)
if ser.isOpen():
     print('Device communication opened on ' + ser.name)

### Initialize pygame ###
pygame.init()
 
resx = 1440
resy = 1280 

screen = pygame.display.set_mode((resx,resy))  # Set resolution for monitor 1440x1200 or w/e
xoff = int(resx/2)
yoff = int(resy/2) 

N_step = 10000
data = np.zeros((N_step,3))

ent1 = 0
ent2 = 0

for i in range(0,N_step):

    ent1_last = ent1
    ent2_last = ent2

    ser.write(b'TX 1000\r')
    x = ser.read_until('\r')
    w = x[8:-9]
    #print(w)
   

    #could not convert string to float: b'0+0161' 
    if w:
        
        print(w)
        ent1 = float(w[1:7])/100
        ent2 = float(w[8:14])/100
        ent3 = float(w[15:21])/100

        if str(w[0]) == '45':
            ent1 = -ent1 
        	
        if str(w[7]) == '45':
            ent2 = -ent2
        
        if str(w[14]) == '45':
            ent3 = -ent3

        data[i,:]=(ent1,ent2,ent3)

        ent1 = int(ent1)
        ent2 = int(ent2)
        
        pygame.draw.circle(screen,(0,0,0),(xoff-ent2_last,yoff+ent1_last),10)
        pygame.draw.circle(screen,(255,255,0),(xoff,yoff),10)
        pygame.draw.circle(screen,(0,0,0),(xoff,yoff),10)
        pygame.draw.circle(screen,(255,0,0),(xoff-ent2,yoff+ent1),10)
        pygame.display.update()

#plt.scatter(data[:,0],data[:,1])
#plt.show()

#fig = plt.figure()
#ax = Axes3D(fig)
#ax.scatter(data[:,1],data[:,2],data[:,3])
#fig.show()


#x = ser.write(b'TSTOP \r')
#time.sleep(2)
#x = ser.read(100)
#print(x)

ser.close()






#insert " " " here

