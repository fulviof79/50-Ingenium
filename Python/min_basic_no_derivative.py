#%%

import matplotlib.pyplot as plt
import numpy as np


#Function to analyze
def f(x):
    return (x**3+5*x**2+3*x-6)

#Numerical approximation of derivative
def ndf(x, derivative_precision=0.01):
    return (f(x+derivative_precision)-f(x))/derivative_precision


#Plot
#Plot parameter, 
plot_xmin=-5
plot_xmax=5
total_points=1000

xvalues= np.linspace(plot_xmin,plot_xmax,total_points)
yvalues = f(xvalues)

plt.axhline(0, color='r')
plt.axvline(0,color='r')
plt.plot(xvalues,yvalues)
plt.ylim(-10, 10)
plt.show()

#define Parameters
#precision
delta=1e-10
#Max number of iterations
max_iterations=10000
#Initial guess
initial_guess=-4
#Learning rate
learning_rate=0.01


guess=initial_guess
for n in range(max_iterations):
    #Follow descent direction
    next_guess = guess + learning_rate*( ndf(guess))
    
    #Stop id desired precision in reached
    if abs(f(next_guess)-f(guess))  < delta:
        break
    
    guess=next_guess
   
#Print results
print("Starting the search at {}".format(initial_guess))
print("Found a local maximum at {}".format(guess) )


# %%
