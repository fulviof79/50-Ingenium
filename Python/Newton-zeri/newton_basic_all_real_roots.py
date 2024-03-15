#%%

import matplotlib.pyplot as plt
import numpy as np

# Define the function f(x)
def f(x):
    return 4*x**4+2*x-1

# Define the derivative of f(x)
def df(x):
    return 16*x**3+2
    
# Generate x and y values for plotting
xvalues= np.linspace(-1,1,100)
yvalues = f(xvalues)

# Plot the function
plt.axhline(0)
plt.plot(xvalues,yvalues)

plt.show()

# Define precision
delta=1e-10

# Define range of initial guesses
x_min=-5
x_max=5
max_iterations=100
amount=100

guess_range=np.linspace(x_min,x_max,amount)

roots=[]

# Iterate over the guess range
for guess in guess_range:
    
    for n in range(max_iterations):
        if df(guess) !=0:
            next_guess = guess - f(guess)/df(guess)
        else:
            break
            #TODO Catch error
        if abs(f(next_guess))< delta:
            already_in = False
            for root in roots:
                if abs(next_guess - root)< delta:
                    already_in = True
                    break
            if not(already_in):
                roots.append(next_guess)
            break
        else:
            guess=next_guess
 
if roots:        
    print("Found {} roots".format(len(roots))) 
    for index,root in enumerate(roots):     
        print("root {} -> {}".format(index,root))

# %%
