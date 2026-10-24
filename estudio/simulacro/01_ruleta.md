# Pregunta 1. Selección por ruleta sin `choice`

## Enunciado

Se tienen seis cromosomas con aptitudes `(10,20,30,40,60,80)`. La población nueva
debe tener seis miembros, seleccionados con reemplazo mediante ruleta.
Calcule las probabilidades de selección y las copias esperadas de cada cromosoma.
Simule **1000 poblaciones nuevas**, no solamente 1000 selecciones, utilizando
acumuladas y `while`. Compare esperanza y observación tanto por población como
en el total de las repeticiones. No use semilla, `choice` ni gráficos.

## Por qué practicar esta variante

Es una modificación directa de PC1 P1 y del método de inversa discreta del TXT
de clase. El cambio de números obliga a reconocer el algoritmo, en vez de copiar
los resultados anteriores. Además, la distinción entre mil poblaciones y mil
selecciones comprueba justamente un punto que puede causar errores de escala.
Aquí se hacen seis selecciones en cada repetición: en total se sortean 6000 miembros.

## Solución matemática y por qué es correcta

La ruleta asigna a cada cromosoma una porción proporcional a su aptitud. No podemos
usar directamente 10 o 80 como probabilidades: primero hay que normalizarlas.
Como la suma es 240, la probabilidad es $p_i=f_i/240$. El cromosoma de aptitud 80
tiene probabilidad $80/240=1/3$: ocupa un tercio de la ruleta, no ocho veces la
población ni ochenta selecciones obligatorias.

Sea $C_i$ el número de copias del cromosoma $i$ dentro de una población. Cada una
de las seis selecciones tiene probabilidad $p_i$ de elegirlo. Escribiendo $C_i$
como suma de seis indicadores y usando linealidad de la esperanza se obtiene:

$$
E[C_i]=\sum_{s=1}^{6}P(\text{selección }s=i)=6p_i.
$$

| Aptitud | Probabilidad | Esperanza por población | Esperanza en 1000 poblaciones |
| ---: | ---: | ---: | ---: |
| 10 | 1/24 | 0.25 | 250 |
| 20 | 1/12 | 0.50 | 500 |
| 30 | 1/8 | 0.75 | 750 |
| 40 | 1/6 | 1.00 | 1000 |
| 60 | 1/4 | 1.50 | 1500 |
| 80 | 1/3 | 2.00 | 2000 |

La suma de esperanzas por población es seis. Para acumular mil poblaciones,
se multiplica cada esperanza por mil. **No se redondea 0.25 a cero:** significa
que, al repetir muchas poblaciones, se obtiene en promedio una copia cada cuatro
poblaciones; no significa que un cromosoma físico se parta en cuatro.

## Código

```python
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
```

## Explicación del código por bloques

**Probabilidades y acumulada.** `p=f/f.sum()` implementa la normalización anterior.
`np.cumsum(p)` convierte las seis probabilidades en fronteras sobre el intervalo
de cero a uno. Por ejemplo, la primera frontera es $1/24$, y la segunda es
$1/24+1/12=1/8$. El largo de cada intervalo es exactamente la probabilidad que
queremos asignar. Por eso un uniforme situado en ese intervalo selecciona al
cromosoma correspondiente: es la justificación probabilística del algoritmo.

**Los dos `for` no hacen lo mismo.** El exterior repite el experimento completo
1000 veces. El interior llena sus seis plazas. Para cada plaza se genera un
uniforme NUEVO; reutilizar el mismo para todas ellas introduciría dependencia y
cambiaría el experimento. No se elimina una cadena después de seleccionarla,
porque el enunciado permite reemplazo y, por tanto, copias repetidas.

**La búsqueda con `while`.** `j` comienza en la primera categoría y avanza mientras
el uniforme esté más allá de su frontera. Al terminar, ese índice es el elegido.
Se usa `>=` para representar intervalos cerrados por la izquierda y abiertos por
la derecha. El límite `j<n-1` evita salir del arreglo por un último decimal de
redondeo numérico; no sustituye la obligación de partir de probabilidades válidas.
La actualización `copias[j]+=1`, escrita explícitamente, cuenta UNA selección.

**Los cinco resultados tienen unidades diferentes.** `p` es probabilidad;
`n*p`, esperanza de copias por población; `k*n*p`, esperanza acumulada;
`copias`, conteo realmente observado; y `copias/k`, promedio observado por
población. Comparar `copias` con `n*p` sería comparar mil poblaciones contra una.
Los contadores usan enteros; que una esperanza se imprima como `250.` no la
convierte en una probabilidad ni indica un error del método.

## Cómo interpretar la salida y adaptar el ejercicio

Los conteos observados deben sumar **exactamente 6000** porque todas las plazas
se llenan. Cada conteo individual estará alrededor de su esperanza, sin que se
exija igualdad exacta. El cromosoma de aptitud 80 puede aparecer 1950 o 2030 veces
sin que eso contradiga su esperanza de 2000; una muestra no es su media teórica.

Si cambian las aptitudes, se conserva el procedimiento y se recalculan las
probabilidades. Si cambia el tamaño de la población, cambia el número de plazas.
Si la consigna dice «1000 selecciones individuales», se hacen 1000 sorteos en
total y la esperanza acumulada pasa a ser $1000p_i$, no $6000p_i$.
