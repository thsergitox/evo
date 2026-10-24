# COPIA DE LECTURA. Fuente: /home/sergi/Documents/semesters/nine/dl/evo/pc1/Sergio_pezo_1er_Lab_Calificado_CS521.ipynb
# Celdas numeradas desde 1. Se preserva el código; no se ejecuta.

# %% [celda 1; markdown]
# # Práctica Calificada 1 - Programación Evolutiva
# 
# Sergio Sebastian Pezo Jimenez  
# 20224087G
# 
# Este notebook es el solucionario de la PC1, cada celda de código tiene sus respectivos comentarios para explicar de manera debida el uso del codigo. Se utilizó una semilla 12 para reproductibilidad

# %% [celda 2; code]
# Importamos numpy
import numpy as np

# %% [celda 3; markdown]
# ## Problema 1
# 
# Usando selección de la ruleta rusa reflejada en la línea 
# 
# `x = np.random.choice(np.arange(n),size=n,replace=True,p=p)`
# 
# Donde `n` es el número de cromosomas que se seleccionan para formar la nueva población y `p` contiene la probabilidad de selección de cada cromosoma según su aptitud, se realizaron 1000 simulaciones.
# 
# El número esperado de copias fue:
# 
# $(0.14634146 \ 0.29268293 \ 0.43902439 \  0.73170732 \ 1.46341463 \ 2.92682927)$
# 
# Obteniendo con la simulación:
# 
# $(0.146 \ 0.260 \ 0.475 \ 0.763 \ 1.479 \ 2.877)$
# 
# Por lo tanto, los valores simulados son cercanos a los valores esperados, verificando el comportamiento de la selección por ruleta.
# 

# %% [celda 4; code]
np.random.seed(12)

# Los valores de aptitud de los seis cromosomas
f = np.array([5, 10, 15, 25, 50, 100])

# El tamaño de la población
n = 6

# El número de simulaciones
k = 1000

# Definimos una semilla para poder obtener los mismos resultados

# Calculamos la probabilidad de selección de cada cromosoma
p = f/np.sum(f)

# Calculamos el número esperado de copias de cada cromosoma
n_esp = n*p

# Creamos un arreglo para acumular las copias obtenidas
copias = np.zeros(n)

# Repetimos el experimento 1000 veces
for i in np.arange(k):
    # Selección de la ruleta rusa
    x = np.random.choice(np.arange(n),size=n,replace=True,p=p)
    # Recorremos los seis posibles cromosomas
    for j in np.arange(n):
        # Contamos cuantas veces fue seleccionado cada cromosoma
        copias[j]=copias[j]+x.tolist().count(j)

# Valores teóricos
print("Numero esperado:")
print(n_esp)

# Copias acumuladas entre las 1000 simulaciones
print("Numero estimado:")
print(copias/k)

# %% [celda 5; markdown]
# ## Problema 2
# 
# Para este problema se usó el conteo de copias con la siguiente línea
# 
# `ncount = f/f_`
# 
# Donde `f` contiene la aptitud de cada cromosoma y `f_` es la aptitud promedio de la población, con esta se obtiene el número de copias correspondiente a cada cromosoma.
# 
# La parte entera, en el código `ent`, de `ncount` representa las copias que se asignan directamente, mientras que la parte fraccionaria se utiliza como probabilidad para obtener una copia adicional mediante
# 
# `if np.random.rand()<frac:`
# 
# El número esperado de copias fue:
# 
# $(0.14634146 \ 0.29268293 \ 0.43902439 \ 0.73170732 \ 1.46341463 \ 2.92682927)$
# 
# Obteniendo con la simulación:
# 
# $(0.154 \ 0.290 \ 0.456 \ 0.715 \ 1.460 \ 2.928)$
# 
# Obteniendo nuevamente valores cercanos, verificando el método de conteo de copias.

# %% [celda 6; code]
np.random.seed(12)

# Usaremos los mismos valores f, n, k del problema 1
# Calculamos la aptitud promedio de la población
f_ = np.mean(f)

# Calculamos el número esperado de copias de cada cromosoma
ncount = f/f_

# Creamos un arreglo para acumular las copias obtenidas
copias = np.zeros(n)

# Simulamos 1000 veces
for i in np.arange(k):
    # Recorremos cada uno de los seis cromosomas
    for j in np.arange(n):
        # Obtenemos la parte entera de ncount
        ent = np.floor(ncount[j])
        # Obtenemos la parte fraccionaria de ncount
        frac = ncount[j]-ent
        # Agregamos siempre la cantidad correspondiente a la parte entera
        copias[j] = copias[j]+ent
        # Generamos un aleatorio para decidir si agregamos una copia adicional
        if np.random.rand() < frac:
            # Agregamos una copia si el aleatorio es menor que la parte fraccionaria
            copias[j] = copias[j]+1

# Número esperado de copias
print("Numero esperado:")
print(ncount*k)

# Calculamos el promedio obtenido en las 1000 simulaciones
print("Numero estimado:")
print(copias)

# %% [celda 7; code]
import numpy as np
import matplotlib.pyplot as plt
k=1000
casos=np.array([5,10,15,25,50,100])
sum_=np.sum(casos)
f_i=casos/sum_;f_medio=np.mean(f_i)
f_i_entre_f_medio=f_i/f_medio
P, P_entera = np.modf(f_i_entre_f_medio)
P_=f_i_entre_f_medio/len(casos)
P_cumsum=np.cumsum(P_)
xx=np.zeros((k,len(P)))

for j in np.arange(k):
  for i in np.arange(len(P)):
    u=np.random.rand(1)
    l=0

  while u>P_cumsum[l]:
    l=l+1
    xx[j,i]=l+1
count_=np.zeros((k,len(P)))
for i in np.arange(k):
  for j in np.arange(len(P)):
    count_[i,j]=xx[i,:].tolist().count(j+1)+P_entera[j]
count__=np.zeros((len(P)))
for s in np.arange(len(P)): count__[s]=np.sum(count_[:,s])
print("Numero esperado:",P_*k*len(P_)+k*P_entera)
print("Numero selecciones:", count__)

# %% [celda 8; markdown]
# ## Problema 3
# 
# Finalmente, usamos una variable aleatoria uniforme discreta de la siguiente con la función `entero_aleatorio(a, b)`
# 
# `np.floor((b-a+1)*np.random.rand())+a`
# 
# Donde `a` es el límite inferior, `b` es el límite superior y `np.random.rand()` genera un número aleatorio entre 0 y 1, se generaron 1000 números enteros entre 3 y 12.
# 
# Como existen 10 valores posibles y todos tienen la misma probabilidad, el número esperado de apariciones de cada valor fue:
# 
# $(100 \ 100 \ 100 \ 100 \ 100 \ 100 \ 100 \ 100 \ 100 \ 100)$
# 
# Obteniendo con la simulación:
# 
# $(90 \ 101 \ 96 \ 97 \ 101 \ 95 \ 107 \ 88 \ 114 \ 111)$
# 
# Por lo tanto, las cantidades obtenidas por simulación son cercanas a las 100 apariciones esperadas para cada número entre 3 y 12.

# %% [celda 9; code]
np.random.seed(12)

# Función con la que generaremos un entero entre un intervalo
def entero_aleatorio(a,b):
    return int(np.floor((b-a+1)*np.random.rand())+a)

# Para este problema solo usaremos el k de los anteriores problemas

# Definimos el límite inferior
a=3

# Definimos el límite superior
b=12

# Creamos un arreglo para guardar los 1000 números generados
x = np.zeros(k)

# Generamos los 1000 números aleatorios
for i in np.arange(k):
    # Aquí es donde generamos un entero aleatorio entre 3 y 12
    x[i]=entero_aleatorio(a,b)

# Creamos un arreglo con todos los posibles valores entre 3 y 12
valores = np.arange(a,b+1)

# Creamos un arreglo para contar cuántas veces aparece cada valor
pesos_ = np.zeros(len(valores))

# Recorremos todos los valores posibles
for j in np.arange(len(valores)):
    # Contamos cuántas veces apareció cada número
    pesos_[j] = x.tolist().count(valores[j])

# Calculamos el número esperado de apariciones de cada valor
esperado = (k/len(valores))*np.ones(len(valores))

# Frecuencias esperadas
print("Numero esperado:")
print(esperado)

# Frecuencias obtenidas
print("Numero obtenido:")
print(pesos_)

