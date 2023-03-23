#%%

import matplotlib.pyplot as plt
import numpy as np



def f(x):
    return x**3-2*x**2-x-3

def df(x):
    return 3*x**2-4*x-1
    
#Plot
#Plot parameter, 
plot_xmin=-1
plot_xmax=3
total_points=1000

xvalues= np.linspace(plot_xmin,plot_xmax,total_points)
yvalues = f(xvalues)

plt.axhline(0, color='r')
plt.axvline(0,color='r')
plt.plot(xvalues,yvalues)

plt.show()

#define precision
delta=1e-10
max_iterations=1000
initial_guess=-1
learning_rate=0.01
roots=[]
min_guess=initial_guess
max_guess=initial_guess

max_min={"min": False , "max" : False}

min_found=False
max_found=False
min_overflow=False
max_overflow=False
for n in range(max_iterations):
    if not(min_found) and not(min_overflow):
        next_min_guess = min_guess - learning_rate*( df(min_guess))
        
    if not(max_found) and not(max_overflow):
        next_max_guess = max_guess + learning_rate*( df(max_guess))

    try:
        
        if abs(f(next_min_guess)-f(min_guess))  < delta:
            max_min["min"]=next_min_guess
            min_found = True
    except:
        min_overflow=True
        
    try:
        if abs(f(next_max_guess)-f(max_guess))  < delta:
            max_min["max"]=max_guess
            max_found = True  
    except:
        max_overflow=True
         
    if (min_found and max_found) or (min_found and max_overflow) or (max_found and min_overflow) or (max_overflow and min_overflow):
        break
    min_guess=next_min_guess
    max_guess=next_max_guess

print("Starting the search at {}".format(initial_guess))
if min_overflow:
    print("Cannot find minimum. Overflow")
else:
   print("Found a local minimum at {}".format(max_min["min"]) )
if max_overflow:
    print("Cannot find maximum. Overflow")
else:
   print("Found a local maximum at {}".format(max_min["max"]) )



# %%
