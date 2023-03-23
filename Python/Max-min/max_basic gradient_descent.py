#%%

import matplotlib.pyplot as plt
import numpy as np



def f(x):
    return x**3-2*x**2+x-3

def df(x):
    return 3*x**2-4*x+1
    
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
initial_guess=-3
learning_rate=0.01


guess=initial_guess
for n in range(max_iterations):
   
    next_guess = guess + learning_rate*( df(guess))
 

    if abs(f(next_guess)-f(guess))  < delta:
        break
    
    guess=next_guess
   

print("Starting the search at {}".format(initial_guess))
print("Found a local maximum at {}".format(guess) )


# %%
