#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 21 19:53:51 2020

@author: reto
"""


import numpy as np
import matplotlib.pyplot as plt

end=6           # tempo finale s
t=0               # tempo iniziale s
dt=0.00001         # delta t
step=0.1          # intervallo di visualizzazione s

v=0               # velocità iniziale m s-1
x=100               # altezza iniziale m
m=0.057           # massa kg
cx=0.47            # coefficiente di forma
d=0.67           # diametro m
A=d*d*np.pi/4        # sezione m2 0.136
rho=1.125         # densità dell'aria km m-3

i=0               # contatore per la visualizzazione
n=0               # contatore per la tabella
f=0               # forze esterne
g=9.81            # accelerazione di gravità

tabella=np.zeros((int(end/step)+1, 5))

tabella[0,0]=t
tabella[0,1]=x
tabella[0,2]=v
tabella[0,3]=-g
tabella[0,4]=f
print(t,round(x,3),round(v,3),round(-g,3),round(f/m,3))
n=n+1

while t <= end:
      f=-0.5*cx*rho*A*v*np.abs(v)   # forza d'attrito
      a=-g+f/m       # accelerazione istantanea
      v=v+a*dt          # velocità istantanea
      x=x+v*dt          # altezza istantanea
      t=t+dt
      t=round(t,8)      # approssimazione per evitare accumulo di errore
      i=i+1
      if i==step/dt:    # visualizzazione
            tabella[n,0]=t
            tabella[n,1]=x
            tabella[n,2]=v
            tabella[n,3]=a
            tabella[n,4]=f
            print(t,round(x,3),round(v,3),round(a,3),round(f/m,3))
            i=0
            n=n+1

plt.rcParams["figure.figsize"] = (15,10)
plt.grid(which='both', axis='both')
plt.minorticks_on()
plt.grid(b=True, which='minor', color='#999999', linestyle='-', alpha=0.2)
#plt.ylim([-0.2,2.5])
plt.scatter(tabella[:,0],tabella[:,1])
plt.show()

plt.rcParams["figure.figsize"] = (15,10)
plt.grid(which='both', axis='both')
plt.minorticks_on()
plt.scatter(tabella[:,0],tabella[:,2])
plt.show()

plt.rcParams["figure.figsize"] = (15,10)
plt.grid(which='both', axis='both')
plt.minorticks_on()
plt.scatter(tabella[:,0],tabella[:,3])
plt.show()
