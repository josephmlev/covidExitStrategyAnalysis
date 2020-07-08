#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
SIR model for Covid19 pandemic. The goal of the model is to analyse weekly trends and test
validity of opening strategies.

Data used in any curve fitting is from JHU GitHub: https://github.com/CSSEGISandData/COVID-19

Author: Steven Sheppard
Date:	7/20/20

'''
import pylab as py
from scipy.integrate import odeint

# Global parameters to define:
mu = # typical death/birth rate "people per timestep" [T**-1]
b = # 
g = # Removal/Recovery Rate 
R = b/(mu+g) # Basic Reproductive Ratio

# Variables for transmission and recovery functions:
A = 1.5; B = .4; C = 1/365; w1 = py.sin(2*py.pi/7); w2 = 1 ;
paramB = (A, B, C, w1, w2)

g = 5/365; d = 0.2; w = 2
paramG = (g, d, w)

# Initial Population values:
N = 1; I0 = .01; E0 = 0.0; R0 = 0.0; S0 = N - I0 - R0
initial_c = (S0, I0, E0, R0)

# Set up the time array. Match data reporting frequency, daily:
dt = 0.1; t0 = 0; tmax = 365
time = py.arange(t0, tmax+dt, dt)

# Build a time dependent Contact Rate function
def Beta(Input, t):
	A, B, C, w1, w2 = Input
	beta = abs(A * py.exp(-w1 * t) * py.sin(w2 * t)) + B - C*t
	return beta


# Build a time dependent mean recovery rate.
def Gamma(Input, t):
	g, d, w = Input
	gamma = g/2 + abs(d*py.sin(w*t))
	return gamma


def diff_eqs(Init, t, InputB, InputG):
	S, I, E, R = Init # Initial conditions
	dSdt = -(B(InputB,t)*S*I/N + mu*(S - 1))
	dIdt = Beta(InputB,t)*S*I/N - (Gamma(InputG, t)*I + mu*I)
	dRdt = Gamma(InputG, t)*I*(1 + mu) - mu*R 
	return dSdt, dIdt, dRdt


# Solve the ODE and split into seperate arrays, this is with wiggle
solution = odeint(diff_eqs, initial_c, time, args=(paramB,paramG))
S, I, R = solution.T

# Plot the results to verify model works
title = 'SIR Model'
py.close('all')
py.figure(figsize=(8,8))
py.title(title)
py.plot(time, S, color='blue', label='Susceptible', linewidth=1.5)
py.plot(time, I, color='red', label='Infected', linewidth=1.5)
py.plot(time, R, color='green', label='Recovered', linewidth=1.5)
py.legend(frameon=True)
py.xlabel('Days'); py.ylabel('People')
py.show()