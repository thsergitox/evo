import numpy as np

f = np.array([10, 20, 30, 40, 60, 80])
n = len(f)
k = 1000
p = f / f.sum()
acumulada = np.cumsum(p)
copias = np.zeros(n).astype(int)

for repeticion in range(k):
    for seleccion in range(n):
        u = np.random.rand()
        j = 0
        while j < n - 1 and u >= acumulada[j]:
            j = j + 1
        copias[j] = copias[j] + 1

print("Probabilidades:", p)
print("Esperanza por poblacion:", n * p)
print("Esperanza en 1000 poblaciones:", k * n * p)
print("Conteos observados:", copias)
print("Promedio observado por poblacion:", copias / k)
