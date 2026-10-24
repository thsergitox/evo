import numpy as np


def crossover_(padre_1, padre_2, corte):
    hijo_1 = np.concatenate((padre_1[:corte], padre_2[corte:]))
    hijo_2 = np.concatenate((padre_2[:corte], padre_1[corte:]))
    return hijo_1, hijo_2


def mutar_bit(bit, pm):
    if np.random.rand() < pm:
        return 1 - bit
    return bit


padre_1 = np.array([1, 0, 1, 1, 0, 1, 1, 0])
padre_2 = np.array([0, 1, 0, 0, 1, 0, 0, 1])
corte = 3
hijo_1, hijo_2 = crossover_(padre_1, padre_2, corte)
print("Primer descendiente:", hijo_1)
print("Segundo descendiente:", hijo_2)

k = 1000
probabilidades = np.array([0.1, 0.01, 0.001])
mutaciones = np.zeros(len(probabilidades)).astype(int)
for j in range(len(probabilidades)):
    pm = probabilidades[j]
    for i in range(k):
        resultado = mutar_bit(0, pm)
        if resultado == 1:
            mutaciones[j] = mutaciones[j] + 1
    print("pm:", pm, "Esperadas:", k * pm, "Observadas:", mutaciones[j])
