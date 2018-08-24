# Generate a Poisson Point Process

# Inputs:
# time step (s) $1
# duration (s) $2
# rate (Hz) $3

import matplotlib.pyplot as plt
import numpy as np
import math
import pandas as pd

def generate_PP(dt,T,rate,N_step):

        #dt = 0.001 
        #T = 10
        #t = np.arange(0,T,dt)
        #N_step = len(t)

        #rate = 8
        binary = [0]*N_step

        for i in range(1,N_step):
                s = np.random.uniform(0,1,1)
                if rate*dt > s:
                        binary[i] = 1

        ind = [index for index, value in enumerate(binary) if value == 1]
        N_spikes = len(ind)
        ind = np.array(ind)
        spk_times = ind*dt
        np.savetxt("spk_times.txt", spk_times,fmt="%2.3f")

        plt.vlines(spk_times,0,2,color='k',linestyles='solid')

        axes = plt.gca()
        axes.set_xlim([0,T])
        plt.xlabel('Time [s]')
        plt.show()

        return binary

def main():

        dt = input('Enter time step:   ')
        dt = float(dt)
        T = input('Enter total time:   ')
        T = float(T)
        rate = input('Enter rate:   ')
        rate = float(rate)
        
        t = np.arange(0,T,dt)
        N_step = len(t)

        binary = generate_PP(dt,T,rate,N_step)
        df = pd.Series(binary)             #df = pd.Series(binary,columns=['t'], index=['train_1'])
        bins = np.transpose(df[1:200])
        print(np.where(bins)) 


main()
