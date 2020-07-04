#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul  3 13:16:23 2020

@author: herbiek9
"""

# -*- coding: utf-8 -*-
"""
Created on Wed May 16 18:53:46 2018

@author: jlevine7
"""
import numpy as np
import scipy.integrate as sp
import matplotlib.pyplot as plt


def seir(y, time, g, k, r):
    S, E, I, R = y

    N = y.sum() #total population, just keep it 1
    b = r * g #day^-1, 
    
    dS = (-b * S * I/N)
    dE = ( b * S * I/N) - (k * E)
    dI = (k * E) - (g * I)
    dR = (g * I)
    
    dydt=[dS,dE,dI,dR]
    return dydt


y = np.zeros(4) # S, E, I, R
y[0] = .99 #Susceptible
y[1] = 0 #Exposed
y[2] = .01 #Infectious
y[3] = 0 #Recovered

g = 1/4 #day^-1, recovery rate
k = 1/3 #day^-1, incubation
r = 2   #dimentionless, reproduction number

tstop = 100 #days
tstep = 10 * tstop
t = np.linspace(0, tstop, tstep) 

sol = sp.odeint(seir, y, t, (g, k, r))


##########
#plotting
##########


plt.close('all')
plt.figure(1)
plt.plot(t, sol[:, 0], label = 'Susceptible')
plt.plot(t, sol[:, 1], label = 'Exposed')
plt.plot(t, sol[:, 2], label = 'Infectious')
plt.plot(t, sol[:, 3], label = 'Recovered')
plt.xlabel('time (days)')
plt.ylabel('percent of population')
plt.legend()























