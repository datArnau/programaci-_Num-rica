#!/usr/bin/env python
# coding: utf-8

# # Pràctica amb programació numèrica

# ## Exercici 1

# In[2]:


import numpy as np


# In[43]:


def resum(matriu):
    
    matriu = np.array(matriu)
    if (matriu.ndim>1):
        print("error")
    else:
        print ("La matriu es " + str(matriu))
        print("La moda es " + str(np.median(matriu)))
        print("La mitjana es " + str(np.mean(matriu)))
        print("La maxima es " + str(np.max(matriu)))
        print("La minima es " + str(np.min(matriu)))
        print("La la variança es " + str(np.var(matriu)))
        print("La desviació estandard es " + str(np.std(matriu)))
    return 0

resum ([4, 2, 5, 2, 6, 3, 6, 12])    
    


# ## Exercici 2

# In[1]:


from random import randint

def rand_matriu(n):
    matriu = []
    for r in range(n):
        fila = []
        for s in range(n):
            fila.append(randint(1,100))
        matriu.append(fila)
    return matriu
resultat = rand_matriu(6)
print(resultat)    
    


# ## Exercici 3
# 

# In[9]:


una_matriu = rand_matriu(4)
files = len(una_matriu)
columnes = len(una_matriu[0])

for r in range(files):
    suma = sum(una_matriu[r])
    una_matriu[r].append(suma)
    
nova_fila = []    
for s in range(columnes):
    suma = sum([fila[s] for fila in una_matriu])
    nova_fila.append(suma)
    
nova_fila.append(sum(nova_fila))
una_matriu.append(nova_fila)
print(una_matriu)
# l'últim valor de cada fila és la suma de la fila
#l'última fila és la suma de les columnes, inclosa la columna de les sumes de les files


# ## Exercici 4

# In[11]:


import numpy as np
import matplotlib.pyplot as plt
x_simple = np.array([-2, -1, 0, 1, 2])
y_simple = np.array([4, 1, 3, 2, 0])
my_rho = np.corrcoef(x_simple, y_simple)

print(my_rho)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




