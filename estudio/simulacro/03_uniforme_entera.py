import numpy as np


def entero_aleatorio(a, b):
    return int(a + np.floor((b - a + 1) * np.random.rand()))


a = -2
b = 5
k = 1000
m = b - a + 1
x = np.zeros(k).astype(int)
conteos = np.zeros(m).astype(int)

for i in range(k):
    x[i] = entero_aleatorio(a, b)

for j in range(m):
    conteos[j] = x.tolist().count(a + j)
    print("Valor:", a + j, "Esperado:", k / m, "Observado:", conteos[j])
