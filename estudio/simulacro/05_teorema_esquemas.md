# Pregunta 5. Segundo problema de esquemas: siguiente generación

## Enunciado

Se tiene la siguiente población de cromosomas de longitud ocho:

| Cromosoma | Aptitud |
| --- | ---: |
| `10000100` | 20 |
| `11010110` | 30 |
| `10100101` | 10 |
| `00011011` | 20 |

Considere el esquema `H=1*0**1**`, selección proporcional a la aptitud, cruce de
un punto con corte uniforme entre las siete posiciones interiores, $p_c=0.7$
y mutación independiente por bit con $p_m=0.01$. Identifique los representantes
de H, calcule orden, longitud definitoria, aptitudes medias, esperanza después
de selección y la **cota usual de primer orden** del teorema de esquemas para
la siguiente generación. Implemente los cálculos y explique la interpretación.

## Por qué practicar esta variante

PC2 P1 e preguntaba por una cota, pero su PDF no suministraba todos los datos
necesarios para una evaluación numérica. Aquí SÍ se proporcionan. La dificultad
no es escribir la fórmula: es identificar sus términos sin confundir la aptitud
del esquema con la suma de aptitudes o su orden con el número de comodines.
Este problema también ejercita el contenido central del capítulo 2 de Goldberg.

## Solución matemática y por qué es correcta

H fija un `1` en la posición 1, un `0` en la 3 y un `1` en la 6. Los asteriscos
no imponen condición. Así, los cromosomas primero y segundo lo representan;
el tercero falla en la posición 3 y el cuarto falla, entre otras, en la posición 1.
Se obtiene **$m(H,t)=2$**, **$o(H)=3$** y **$\delta(H)=6-1=5$**. La longitud
total sigue siendo ocho: no se reemplaza $l$ por el orden.

Las aptitudes medias son:

$$
\bar f=\frac{20+30+10+20}{4}=20,
\qquad f_H=\frac{20+30}{2}=25.
$$

Con selección proporcional, la esperanza de representantes después de selección
es $m(H,t)f_H/\bar f=2(25/20)=2.5$. Puede comprobarse también sumando las
probabilidades de sus dos representantes: ocupan $(20+30)/80=0.625$ de la ruleta
y se llenan cuatro plazas; por eso se esperan $4(0.625)=2.5$ copias del esquema.
Son dos maneras de llegar a la misma cantidad.

Un corte puede separar las posiciones fijas extremas en cinco de los siete
lugares interiores. Considerando que solo se cruza con probabilidad 0.7, la cota
de supervivencia por cruce es $1-0.7(5/7)=0.5$. Es una cota conservadora porque
un cruce dentro de ese tramo no necesariamente destruye el esquema si el otro
padre aporta los mismos bits necesarios. La probabilidad de NO alterar sus tres
bits fijos por mutación es $(1-0.01)^3=0.970299$.

La forma usual de primer orden solicitada combina selección y pérdidas:

$$
E[m(H,t+1)\mid P_t]\ge
m(H,t)\frac{f_H}{\bar f}
\left[1-p_c\frac{\delta(H)}{l-1}-o(H)p_m\right].
$$

$$
\text{Cota}=2\frac{25}{20}
\left[1-0.7\frac57-3(0.01)\right]
=2.5(0.47)=\boxed{1.175}.
$$

La cantidad entre corchetes usa la forma de primer orden del libro, no la
probabilidad exacta de que toda la población produzca un número particular de
copias. No debe confundirse con multiplicar ambas supervivencias: el producto
$2.5(0.5)(0.970299)=1.21287375$ conserva términos que la expresión linealizada
no conserva. En esta pregunta se reporta la forma que se pidió: **1.175**.

## Código

```python
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
```

## Explicación del código por bloques

**Identificar representantes con dos bucles.** Para cada cromosoma se comienza
suponiendo `compatible=True`. El bucle interior revisa las ocho posiciones y solo
compara las que no tienen `*`. Una discrepancia vuelve falsa la compatibilidad;
encontrar después otra posición correcta no debe volverla verdadera. Al terminar,
solo las cadenas compatibles aumentan `m` y contribuyen a `suma_H`. Por eso no
se suman por accidente las aptitudes de toda la población al promedio del esquema.

**Orden y extremos fijos.** El siguiente recorrido incrementa `orden` por cada
símbolo fijo. `primera=-1` significa que aún no se encontró ninguno. Al aparecer
el primero se guarda su índice; `ultima` se actualiza con cada símbolo fijo.
La resta es cinco aunque Python use índices 0, 2 y 5: trasladar ambos extremos
una unidad no cambia su distancia. No se suma uno a esa resta.

**Promedios y cota.** `f.sum()/n` usa todos los individuos, mientras `suma_H/m`
usa solamente los representantes. En ESTOS datos $m=2$, por lo que la división
está definida; si se cambia H por uno sin representantes, primero debe reconocerse
esa situación y no calcular un promedio inexistente. El resto del bloque
traslada término por término las fórmulas del desarrollo, sin valores inventados.

**Lectura de la salida.** El valor puede mostrarse como `1.1749999999999998` por
representación binaria de decimales en la computadora. Es el mismo resultado
numérico 1.175 dentro de la precisión de cálculo; no significa que falten copias.
La forma legible del resultado se presenta en el desarrollo matemático.

## Qué significa la respuesta y qué NO significa

La cota se refiere a una **esperanza condicionada a la población actual**. No
garantiza que cada realización tenga al menos dos individuos del esquema; un
conteo real podría ser cero, uno u otro entero. Redondear la cota hacia arriba y
presentarla como mínimo garantizado sería cambiar el significado del teorema.
Tampoco garantiza encontrar el óptimo global: describe propagación de esquemas
bajo operadores y supuestos concretos, no el éxito absoluto de cualquier búsqueda.

Si cambian H o la población, se deben volver a determinar representantes y ambos
promedios. Si solo cambian las tasas, se conservan esas cantidades pero se recalculan
las supervivencias. Si el cruce deja de ser de un punto, no debe copiarse sin
justificación el factor $\delta(H)/(l-1)$.
