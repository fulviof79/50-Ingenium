#%%

import matplotlib.pyplot as plt
import numpy as np


#Function to analyze
def f(x):
    return (x**2-2)/np.exp(x)-3

#Numerical approximation of derivative
def ndf(x, derivative_precision=0.01):
    return (f(x+derivative_precision)-f(x))/derivative_precision


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

#define Parameters
#precision
delta=1e-10
#Max number of iterations
max_iterations=10000
#Initial guess
initial_guess=2
#Learning rate
learning_rate=0.01


guess=initial_guess
for n in range(max_iterations):
    #Follow descent direction
    next_guess = guess - learning_rate*( ndf(guess))
    
    #Stop id desired precision in reached
    if abs(f(next_guess)-f(guess))  < delta:
        break
    
    guess=next_guess
   
#Print results
print("Starting the search at {}".format(initial_guess))
print("Found a local minimum at {}".format(guess) )


# %%
