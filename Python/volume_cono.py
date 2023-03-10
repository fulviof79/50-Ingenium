# %%
import matplotlib.pyplot as plt
import numpy as np
#%%
def disc_area(radius,height,x):
    '''
    Ritorna l'area della sezione (disco) a distanza x dal vertice di un cono ri raggio=radius e altezza=height
    '''
    return (np.pi * radius**2 / height **2 * x**2)

def volume_out(radius,height,slices):
    '''
    Ritorna il volume approssimato dall'esterno di un cono ri raggio=radius e altezza=height
    '''
    x=np.linspace(start=height,stop=0,num=slices, endpoint=False)
    
    area_disco = disc_area(radius,height,x)
    volume_cilindro=area_disco*x[-1]
    return   volume_cilindro.sum()

def volume_in(radius,height,slices):
    '''
    Ritorna il volume approssimato dall'interno di un cono ri raggio=radius e altezza=height
    '''
    x=np.linspace(start=0,stop=height,num=slices,endpoint=False)
    
    area_disco = disc_area(radius,height,x)
    volume_cilindro=area_disco*x[1]
    return   volume_cilindro.sum()
# %%
# Parametri cono 
radius = 5
height= 4
#Precisione : numero di suddivisioni (slices)
precision=10**6


v_out=volume_out(radius,height,precision)
v_in=volume_in(radius,height,precision)
v_average=(volume_out(radius,height,precision)+volume_in(radius,height,precision))/2

print("Raggio={} Altezza={} \n\n Volume con dischi esterni = {}  \n Volume con dischi interni ={} \n Media ={}".format(radius, height,v_out,v_in,v_average))

# %%
# Plot dell'andamento dell area dei dischi e quindi del volume
slices=50
x_out=np.linspace(start=height,stop=0,num=slices,endpoint=False)
x_in=np.linspace(start=0,stop=height,num=slices,endpoint=False)

plt.bar(x_out,disc_area(radius,height,x_out),width=x[-1], color='red')
#plt.bar(x_in,disc_area(radius,height,x_in),width=x_in[1], color='blue')

# %%
