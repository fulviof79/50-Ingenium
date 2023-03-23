#%%
from matplotlib.cbook import delete_masked_points
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

delta=1e-10

rvalues= np.linspace(-5,5,100)
ivalues= np.linspace(-5,5,100)

roots=[]

for r in rvalues:
    for i in ivalues:
        guess= r + i*1j
        for n in range(100):
            if df(guess) !=0:
                next_guess = guess - f(guess)/df(guess)
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
            
print(roots)

# %%
