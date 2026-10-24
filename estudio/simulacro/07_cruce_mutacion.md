# Pregunta 7. Dos descendientes y conteo de mutaciones

## Enunciado

Implemente una función de cruzamiento simple que reciba dos padres binarios y
una posición de corte, y retorne **dos descendientes complementarios**. Aplíquela
a `10110110` y `01001001`, cortando después de los primeros tres bits.
Luego implemente una función que invierta un bit con probabilidad $p_m$.
Para cada $p_m\in\{0.1,0.01,0.001\}$, haga 1000 llamadas independientes, comenzando
con bit cero EN CADA llamada, y compare el número esperado y observado de
mutaciones. No grafique ni fije semilla.

## Por qué practicar esta variante

La dirigida pide explícitamente dos hijos y una función de mutación. El feedback
de PC2 P3 también insiste en generar dos cromosomas. Este ejercicio aísla los
operadores para que puedas comprobar qué entra y qué sale antes de introducirlos
en un algoritmo completo. Así no se confunde el tamaño de la población con la
cantidad de descendientes producidos por UNA pareja.

## Solución matemática y por qué es correcta

Separando cada padre después de sus primeros tres bits:

```text
Padre 1: 101 | 10110
Padre 2: 010 | 01001

Hijo 1:  101 | 01001 = 10101001
Hijo 2:  010 | 10110 = 01010110
```

El primer hijo hereda el prefijo del primer padre y el sufijo del segundo;
el segundo combina los segmentos opuestos. Se conserva la longitud ocho.
Ambos nacen de los mismos padres y del mismo corte, por lo que son complementarios
en el sentido del intercambio, aunque sus bits no tengan por qué ser opuestos
en todos los ejemplos posibles. Si ambos padres tienen el mismo bit en una posición,
los dos hijos también pueden coincidir allí.

Para mutación, sea $U$ uniforme independiente. El nuevo bit es $1-b$ si
$U<p_m$ y permanece $b$ en otro caso. Como el intervalo $[0,p_m)$ tiene longitud
$p_m$, la probabilidad de invertirlo es exactamente $p_m$. Si $M$ cuenta
mutaciones en mil llamadas, por linealidad:

$$
E[M]=1000p_m.
$$

Se esperan **100, 10 y 1 mutaciones**, respectivamente. Son esperanzas del
conteo, no de la proporción: las proporciones teóricas serían 0.1, 0.01 y 0.001.
Cada llamada vuelve a empezar en cero, de modo que un resultado uno identifica
sin ambigüedad una mutación en esa llamada.

## Código

```python
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
```

## Explicación del código por bloques

**El contrato de `crossover_`.** La función no elige padres ni introduce una
probabilidad de cruce, porque esos datos ya están fijados por la pregunta. Su
única tarea es intercambiar los segmentos y entregar ambos resultados. El slice
`[:corte]` contiene los tres primeros bits y `[corte:]` los restantes.
`np.concatenate` une segmentos; usar `+` sobre arrays haría una suma elemento
a elemento y NO el cruzamiento solicitado.

**No se destruyen los padres.** Los hijos se construyen como arreglos nuevos y
se devuelven juntos. Si se sobrescribiera el primer padre antes de construir
el segundo sin conservar su información, este último podría usar segmentos ya
modificados. El código evita ese problema al no modificar los arreglos de entrada.
No hace falta una población de tamaño dos para demostrar que se generan dos hijos:
lo que importa es la pareja de valores retornada por la función.

**La función `mutar_bit`.** Hace UN sorteo y devuelve el bit transformado o el
original. La expresión `1-bit` funciona porque el dominio está restringido a cero
y uno: invierte cualquiera de esos dos casos. No elige un bit nuevo al azar con
probabilidad 1/2, pues eso introduciría una probabilidad de cambio diferente.
También sería incorrecto invertir siempre el bit y usar $p_m$ solamente como rótulo.

**Los dos bucles del experimento.** El exterior selecciona una de las tres tasas.
El interior realiza mil llamadas para esa tasa. Se llama siempre con cero inicial,
en vez de pasar a la siguiente llamada el resultado de la anterior. Si se encadenan
los estados y al final se mira solo si quedó cero o uno, se mide la PARIDAD de
los cambios, no el número de mutaciones; dos inversiones vuelven al estado inicial.

## Cómo leer resultados y adaptar el ejercicio

El cruce es determinista con estos padres y este corte, por lo que siempre debe
dar las dos cadenas calculadas. Las mutaciones no lo son: observar cero cambios
cuando $p_m=0.001$ es compatible con una esperanza de uno. Tampoco hay que ajustar
el contador para que termine exactamente en 100, 10 o 1.

Si mutas UN cromosoma completo, el sorteo se hace por cada posición. En una
cadena de ocho bits con probabilidad $p_m$ por bit, la esperanza de bits mutados
es $8p_m$, pero la probabilidad de que la cadena no cambie es $(1-p_m)^8$.
Son preguntas distintas. El algoritmo de la pregunta 8 aplica precisamente el
sorteo por posición y mantiene separados el operador de cruce y el de mutación.
