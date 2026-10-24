import numpy as np

limites = np.array([[-3, 5], [0, 1000], [-0.5, 0.5]])
precision = np.array([0.1, 10, 0.001])
puntos = np.array([[-3, 0, -0.5], [5, 1000, 0.5], [1, 500, 0.125]])
longitudes = np.zeros(3).astype(int)

for i in range(3):
    a = limites[i, 0]
    b = limites[i, 1]
    l = 1
    while (b - a) / (2**l - 1) > precision[i]:
        l = l + 1
    longitudes[i] = l

total_bits = int(longitudes.sum())
cromosomas = np.zeros((len(puntos), total_bits)).astype(int)
decodificados = np.zeros((len(puntos), 3))
print("Bits por variable:", longitudes)
print("Total de bits:", total_bits)

for t in range(len(puntos)):
    inicio = 0
    for i in range(3):
        a = limites[i, 0]
        b = limites[i, 1]
        l = longitudes[i]
        d = int(np.floor((puntos[t, i] - a) * (2**l - 1) / (b - a) + 0.5))
        resto = d

        for j in range(l - 1, -1, -1):
            cromosomas[t, inicio + j] = resto % 2
            resto = resto // 2

        d_leido = 0
        for j in range(l):
            d_leido = 2 * d_leido + cromosomas[t, inicio + j]
        decodificados[t, i] = a + (b - a) * d_leido / (2**l - 1)
        inicio = inicio + l

    print("Punto:", puntos[t])
    print("Cromosoma concatenado:", cromosomas[t])
    print("Punto decodificado:", decodificados[t])
