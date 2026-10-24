# COPIA DE LECTURA. Fuente: /home/sergi/Documents/semesters/nine/dl/evo/pc2/PezoSergio_PC2.ipynb
# Celdas numeradas desde 1. Se preserva el código; no se ejecuta.

# %% [celda 1; markdown]
# # Computación Evolutiva - PC2
# 
# - Sergio Sebastian Pezo Jimenez
# - 20224087G

# %% [celda 2; code]
import numpy as np

# %% [celda 3; code]
print("xd")

# %% [celda 4; markdown]
# ## Pregunta 1

# %% [celda 5; code]
# Primero tenemos que calcular cuantos bits necesitamos
puntos = 2097152
l = 0
while 2**l < puntos:
    l += 1

# Individuos
n = 50

print("Bits:", l)

# a)
print("a) Número total de esquemas", 3**l)

# b)
print("b) Número total e puntos de búsqueda", 2**l)

# c)
print("c) Número de esquemas por individuo", 2**l)

# d)
print("d) Inferior:", 2**l, "Superior:", n*2**l)

# d) y e) Nos piden calcular una cotas, así que definiremos un esquema, para trabajar en base a el
# Individuos que pertenecen al esquema H
m = 10
# Aptitud promedio del esquema
fH = 12
# Aptitud de los otros 40 individuos
f_otros = 9.5
# Probabilidad de cruzamiento
pc = 0.25
# Probabilidad de mutacion
pm = 0.01

# Dos posiciones fijas: 11*******************
orden = 2
# Distancia entre las posiciones fijas
delta = 1

# Aptitud promedio de toda la poblacion n definida al inicio
f_prom = (m*fH + (n-m)*f_otros)/n

# Cota inferior por el teorema de esquemas
cota = m*(fH/f_prom)*(1-pc*delta/(l-1)-orden*pm)

print("e) Aptitud promedio:", f_prom)
print("e) Cota inferior esperada:", cota)

# %% [celda 6; markdown]
# # Pregunta 2

# %% [celda 7; code]
# Definimos los limites x, y, z  de las variables x, y, z, respectivamente
limites = [(-20, 125), (0, 1200000), (-0.1, 1)]
precision = [0.5, 10000, 0.001]

# Calculamos la cantidad minima de bits por variable con la precisiones deseadas
longitudes = []
for i in range(3):
    a, b = limites[i]
    l = int(np.ceil(np.log2((b-a)/precision[i] + 1)))
    longitudes.append(l)

print("Bits:", longitudes)
print("El número mínimo de bits es:", sum(longitudes))

puntos = [(-20, 0, -0.1), (125, 1200000, 1), (50, 100000, 0.597)]

# Calculamos la cadena binaria para cada punto
for punto in puntos:
    codigos = []
    valores = []

    for i in range(3):
        a, b = limites[i]
        l = longitudes[i]

        # Convertimos el valor real a un entero
        entero = round((punto[i]-a)/(b-a)*(2**l-1))

        # Pasamos el entero a binario usando l bits
        codigos.append(format(entero, "0"+str(l)+"b"))

        # Decodificamos para comprobar la aproximacion
        valores.append(a+(b-a)*entero/(2**l-1))

    print("Punto:", punto)
    print("Binarios:", *codigos)
    print("Concatenado:", "".join(codigos))
    print("Decodificado:", valores)

# %% [celda 8; markdown]
# # Pregunta 3
# 
# 
# Trabajaremos para el intervalo de [-5, 8]

# %% [celda 9; code]
np.random.seed(7)


X_BOUND = [-5.0, 8.0]

# Definimos nuestros parametros para el algoritmo genetico
n = 2
bits = 12
pc = 0.25
pm = 0.01
generaciones = 150

def F(x):
    return 3*x**10


def get_fitness(valores):
    return valores + 1e-3

def translateDNA(pop):
    pesos = 2**np.arange(bits)[::-1]
    return X_BOUND[0] + (X_BOUND[1]-X_BOUND[0])*pop.dot(pesos)/(2**bits-1)

# Seleccion por ruleta
def select(pop, fitness):
    ps = fitness/fitness.sum()
    indices = np.random.choice(np.arange(n), size=n, replace=True, p=ps)
    return pop[indices]

# Cruzamiento de un punto entre dos cromosomas por corte
def crossover(padre, pop):
    if np.random.rand() < pc:
        j = np.random.randint(n)
        corte = np.random.randint(1, bits)
        padre[corte:] = pop[j, corte:]
    return padre

# Para la mutacion, simplemente cambiaremos un bit con probabilidad pm
def mutate(hijo):
    for j in range(bits):
        if np.random.rand() < pm:
            hijo[j] = 1 - hijo[j]
    return hijo

# Crear poblacion inicial
pop = np.random.randint(2, size=(n, bits))

for t in range(generaciones):
    # Evaluamos los individuos
    valores = F(translateDNA(pop))
    fitness = get_fitness(valores)

    # Guardamos el mejor cromosoma
    mejor = pop[np.argmax(valores)].copy()

    # Imprimimos el progreso cada 10 generaciones
    if t == 0 or (t+1) % 10 == 0:
        print("Generacion", t+1, "Mejor:", np.max(valores))

    # Seleccionamos y generamos descendientes
    pop = select(pop, fitness)
    copia = pop.copy()

    for i in range(n):
        hijo = crossover(pop[i].copy(), copia)
        pop[i] = mutate(hijo)

    # Conservamos al mejor individuo (elitismo)
    pop[0] = mejor

# Resultado final
x = translateDNA(pop)
valores = F(x)

print("Mejor x:", x[np.argmax(valores)])
print("Maximo f(x):", np.max(valores))

