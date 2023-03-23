#%%

import matplotlib.pyplot as plt
import numpy as np



def f(x):
    return 4*x**4+2*x-1

def df(x):
    return 16*x**3+2
    
xvalues= np.linspace(-1,1,100)
yvalues = f(xvalues)

plt.axhline(0)
plt.plot(xvalues,yvalues)

plt.show()

#define precision
delta=1e-10
#range of initial guesses
x_min=-5
x_max=5
max_iterations=100
amount=100

guess_range=np.linspace(x_min,x_max,amount)

roots=[]

for guess in guess_range:
    for n in range(max_iterations):
        if df(guess) !=0:
            next_guess = guess - f(guess)/df(guess)
        else:
            break
            #TODO Catch error
        if abs(next_guess-guess)< delta:
            already_in = False
            for root in roots:
                if abs(next_guess - root)< delta:
                    already_in = True
                    break
            if not(already_in):
                roots.append(next_guess)
            break
        guess=next_guess
 
if roots:        
    print("Found {} roots".format(len(roots))) 
    for index,root in enumerate(roots):     
        print("root {} -> {}".format(index,root))

# %%
