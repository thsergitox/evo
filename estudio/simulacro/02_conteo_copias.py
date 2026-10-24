import numpy as np

f = np.array([10, 20, 30, 40, 60, 80])
n = len(f)
k = 1000
f_promedio = f.sum() / n
ncount = f / f_promedio
copias = np.zeros(n).astype(int)

for repeticion in range(k):
    for j in range(n):
        entera = int(np.floor(ncount[j]))
        fraccion = ncount[j] - entera
        copias[j] = copias[j] + entera
        if np.random.rand() < fraccion:
            copias[j] = copias[j] + 1

print("Aptitud promedio:", f_promedio)
print("Esperanza por realizacion:", ncount)
print("Esperanza en 1000 realizaciones:", k * ncount)
print("Conteos observados:", copias)
print("Promedio observado:", copias / k)
print("Total esperado:", k * n)
print("Total observado:", copias.sum())
