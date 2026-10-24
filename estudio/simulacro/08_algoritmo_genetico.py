import numpy as np
import matplotlib.pyplot as plt


def F(x):
    return 2 * x**4 + 1


def translateDNA(pop):
    pesos = 2**np.arange(bits)[::-1]
    return a + (b - a) * pop.dot(pesos) / (2**bits - 1)


def select(pop, fitness):
    p = fitness / fitness.sum()
    acumulada = np.cumsum(p)
    seleccionados = pop.copy()
    for i in range(len(pop)):
        u = np.random.rand()
        j = 0
        while j < len(pop) - 1 and u >= acumulada[j]:
            j = j + 1
        seleccionados[i] = pop[j]
    return seleccionados


def crossover_(padre_1, padre_2, corte):
    hijo_1 = np.concatenate((padre_1[:corte], padre_2[corte:]))
    hijo_2 = np.concatenate((padre_2[:corte], padre_1[corte:]))
    return hijo_1, hijo_2


def mutate(hijo):
    for j in range(len(hijo)):
        if np.random.rand() < pm:
            hijo[j] = 1 - hijo[j]
    return hijo


a = -2
b = 3
precision = 0.01
bits = 1
while (b - a) / (2**bits - 1) > precision:
    bits = bits + 1

n = 20
pc = 0.8
pm = 0.01
generaciones = 80
pop = np.random.randint(2, size=(n, bits))
mejores = np.zeros(generaciones + 1)
mejores[0] = np.max(F(translateDNA(pop)))

for t in range(generaciones):
    fitness = F(translateDNA(pop))
    padres = select(pop, fitness)
    nueva = padres.copy()

    for i in range(0, n, 2):
        hijo_1 = padres[i].copy()
        hijo_2 = padres[i + 1].copy()
        if np.random.rand() < pc:
            corte = np.random.randint(1, bits)
            hijo_1, hijo_2 = crossover_(padres[i], padres[i + 1], corte)
        nueva[i] = mutate(hijo_1)
        nueva[i + 1] = mutate(hijo_2)

    pop = nueva
    mejores[t + 1] = np.max(F(translateDNA(pop)))

x = translateDNA(pop)
valores = F(x)
indice = np.argmax(valores)
print("Bits:", bits)
print("Paso de la malla:", (b - a) / (2**bits - 1))
print("Mejor cromosoma final:", pop[indice])
print("Mejor x de la poblacion final:", x[indice])
print("Valor encontrado:", valores[indice])
print("Maximo teorico de referencia:", F(b))
plt.plot(np.arange(generaciones + 1), mejores)
plt.title("Mejor aptitud por generacion; referencia teorica: 163")
plt.show()
