### Poisson trains to switch model ###

# Inputs:
# time step (s) $1
# duration (s) $2
# rate (Hz) $3

import matplotlib.pyplot as plt
import numpy as np
import math
import pandas as pd

def generate_PP(dt,T,rate):

        #dt = 0.001 
        #T = 10
        t = np.arange(0,T,dt)
        N_step = len(t)

        #rate = 8
        binary = [0]*N_step

        for i in range(1,N_step):
                s = np.random.uniform(0,1,1)
                if rate*dt > s:
                        binary[i] = 1

        return binary
        
        #ind = [index for index, value in enumerate(binary) if value == 1]
        #N_spikes = len(ind)
        #ind = np.array(ind)
        #spk_times = ind*dt
        #np.savetxt("spk_times.txt", spk_times,fmt="%2.3f")

        #plt.vlines(spk_times,0,2,color='k',linestyles='solid')

        #axes = plt.gca()
        #axes.set_xlim([0,T])
        #plt.xlabel('Time [s]')
        #plt.show()

def switch(x,binary,T,dt,N_step):

    r = 0.61
    c_0 = 0.01
    #c = c_0 + 
    tau = 0.01

    for i in range(1,N_step):
          x[i+1] = x[i] + (dt/tau)*(c_0 - r*x[i] + (x[i]**2)/(1+x[i]**2)) 	
          return x


def main():
        
    # User inputs
    dt = input('Enter time step:   ')
    dt = float(dt)
    T = input('Enter total time:   ')
    T = float(T)
    rate = input('Enter rate:   ')
    rate = float(rate)
    N_runs = input('Enter number of spike trains:   ')
    N_runs = int(N_runs)   
     
    # Initialize variables
    t = np.arange(0,T,dt)
    N_step = len(t)
    x = np.zeros((N_runs,N_step))        
    binary = np.zeros((N_runs,N_step))
        
    for i in range(1,N_runs):
          binary[i,:] = generate_PP(dt,T,rate)
          x[i,:] = switch(x[i,:],binary[i,:],T,dt,N_step)
            
        #spike_index = pd.DataFrame(,
        #                  columns=["binary", 
        #                           "x",
        #                          ],
        #                  index=True)

          plt.plot(t,x)
     
main()
plt.show()
