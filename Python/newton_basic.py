#%%

import matplotlib.pyplot as plt
import numpy as np



def f(x):
    return 4*x**4+2*x-1

def df(x):
    return 16*x**3+2


xvalues= np.linspace(-1,1,100)
yvalues = f(xvalues)

#Plot
#Plot parameter, 
plot_xmin=-1
plot_xmax=1
total_points=1000

xvalues= np.linspace(plot_xmin,plot_xmax,total_points)
yvalues = f(xvalues)

plt.axhline(0, color='r')
plt.axvline(0,color='r')
plt.plot(xvalues,yvalues)

plt.show()
#define precision
delta=1e-10
#range of initial guesses
x_min=-1
x_max=1
max_iterations=100
amount=100


# Initial guess
initial_guess=-0.55


#Main algorithm
guess=initial_guess
for n in range(max_iterations):
    if df(guess) !=0:
        next_guess = guess - f(guess)/df(guess)
    else:
        break
        #TODO Catch error
    if abs(next_guess-guess)< delta:
        break
    guess=next_guess

#Print result
print("Starting with initial guess at {}".format(initial_guess))
print("root at {}".format(guess))

# %%
