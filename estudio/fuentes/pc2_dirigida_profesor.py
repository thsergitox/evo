# TRANSCRIPCIÓN DE LECTURA; NO CORREGIDA NI AUTÓNOMA.
# Fuente: /home/sergi/Documents/semesters/nine/dl/evo/pc2/2doLabDirigido_CS521_.pdf
# Solo se transcriben los dos bloques de código impresos.

# %% Selección por acumuladas
import numpy as np
import matplotlib.pyplot as plt
k=20
P=np.array([0.1,0.2,0.05,0.15,0.0,0.11,0.07,0.04,0.12,0.16])
P_cumsum=np.cumsum(P)
xx=np.zeros((k,len(P)))
for j in np.arange(k):
  for i in np.arange(len(P)):
     u=np.random.rand(1)
     l=0
     while u>P_cumsum[l]:
       l=l+1
     xx[j,i]=l+1

# %% Cruzamiento con dos descendientes
DNA_SIZE = 10
POP_SIZE = 50

pop = np.random.randint(2, size=(POP_SIZE, DNA_SIZE))
i_ = np.random.randint(0, POP_SIZE, size=None)
j_ = np.random.randint(0, POP_SIZE, size=None)

parent_1=pop[i_,:]; print(parent_1)
parent_2=pop[j_,:]; print(parent_2)
cross_point = np.random.randint(DNA_SIZE-1, size=None)
def crossover_(parent_1,parent_2,cross_point):
    parent_1_aux=parent_1.copy()
    parent_1=np.concatenate((parent_1[0:cross_point],parent_2[cross_point:DNA_SIZE]))
    parent_2=np.concatenate((parent_2[0:cross_point],parent_1_aux[cross_point:DNA_SIZE]))
    return cross_point, parent_1, parent_2

crossover_(parent_1,parent_2,cross_point)

