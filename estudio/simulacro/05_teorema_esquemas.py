import numpy as np

cromosomas = ["10000100", "11010110", "10100101", "00011011"]
f = np.array([20, 30, 10, 20])
H = "1*0**1**"
pc = 0.7
pm = 0.01
n = len(cromosomas)
l = len(H)
m = 0
suma_H = 0

for i in range(n):
    compatible = True
    for j in range(l):
        if H[j] != "*" and H[j] != cromosomas[i][j]:
            compatible = False
    if compatible:
        m = m + 1
        suma_H = suma_H + f[i]
        print("Representante:", cromosomas[i])

orden = 0
primera = -1
ultima = -1
for j in range(l):
    if H[j] != "*":
        orden = orden + 1
        if primera == -1:
            primera = j
        ultima = j

delta = 0
if orden > 0:
    delta = ultima - primera

f_promedio = f.sum() / n
f_H = suma_H / m
esperado_seleccion = m * f_H / f_promedio
supervivencia_cruce = 1 - pc * delta / (l - 1)
supervivencia_mutacion = (1 - pm)**orden
cota = esperado_seleccion * (1 - pc * delta / (l - 1) - orden * pm)

print("Representantes actuales:", m)
print("Orden:", orden, "Longitud definitoria:", delta)
print("Aptitud media poblacional:", f_promedio)
print("Aptitud media del esquema:", f_H)
print("Esperanza despues de seleccion:", esperado_seleccion)
print("Cota de supervivencia por cruce:", supervivencia_cruce)
print("Probabilidad de no alterar los bits fijos:", supervivencia_mutacion)
print("Cota usual de primer orden para la esperanza:", cota)
