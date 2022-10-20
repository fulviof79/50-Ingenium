#%%

import matplotlib.pyplot as plt
import numpy as np



def f(x):
    return (x**2-2)/np.exp(x)-3

derivative_precision=0.01
def ndf(x):
    return (f(x+derivative_precision)-f(x))/derivative_precision
    
xvalues= np.linspace(-1,3,100)
yvalues = f(xvalues)

plt.axhline(0)
plt.plot(xvalues,yvalues)

plt.show()

#define precision
delta=1e-10
max_iterations=10000
initial_guess=2
learning_rate=0.01


guess=initial_guess
for n in range(max_iterations):
   
    next_guess = guess - learning_rate*( ndf(guess))
    

    if abs(f(next_guess)-f(guess))  < delta:
        break
    
    guess=next_guess
   

print("Starting the search at {}".format(initial_guess))
print("Found a local minimum at {}".format(guess) )


# %%
