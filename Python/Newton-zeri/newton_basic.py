#%%

from matplotlib.lines import lineStyles
import matplotlib.pyplot as plt
import numpy as np


#Define function f
def f(x):
    return 4*x**4+2*x-1

#Define derivative of the function f
def df(x):
    return 16*x**3+2

#Plot

#Plot parameters, 
plot_xmin=-1
plot_xmax=1
total_points=1000
#Calculate total_points sample of function f (for the plot)
xvalues= np.linspace(plot_xmin,plot_xmax,total_points)
yvalues = f(xvalues)

#Prepare and draw figure
fig = plt.figure() 
ax = fig.add_subplot(1,1,1)
#Dashed axes
ax.axhline(0, color='k', linestyle='--')
ax.axvline(0,color='k', linestyle='--')
ax.set_ylim(min(yvalues)-2,max(yvalues)+1)
#Plot samples of function f
ax.plot(xvalues,yvalues)




#define precision
delta=1e-10
#range of initial guesses
x_min=-1
x_max=1
max_iterations=100
amount=100


# Initial guess
initial_guess=-1

ERROR=False
#Main algorithm
guess=initial_guess
for n in range(max_iterations):
    if df(guess) !=0:
        next_guess = guess - f(guess)/df(guess)
    else:
        print("Error : derivative is 0 at x={}".format(guess))
        ERROR=True
        break
        
    if abs(next_guess-guess)< delta:
        break
    guess=next_guess

#Print result
if not(ERROR):
    print("Starting with initial guess at {}".format(initial_guess))
    print("root at {}".format(guess))

ax.plot(guess, f(guess), 'or')

ax.annotate("{:.2f}".format(guess), # this is the text
                 (guess,f(guess)), # these are the coordinates to position the label
                 textcoords="offset points", # how to position the text
                 xytext=(0,-20), # distance from text to points (x,y)
                 ha='center')



# %%
