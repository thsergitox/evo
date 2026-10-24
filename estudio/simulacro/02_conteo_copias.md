# Pregunta 2. Parte entera y copia adicional aleatoria

## Enunciado

Use las aptitudes `(10,20,30,40,60,80)`. Para cada cromosoma defina
$a_i=f_i/\bar f$. En cada realización asigne la parte entera de $a_i$ como copias
seguras y una copia adicional con probabilidad igual a su parte fraccionaria.
Calcule la esperanza de copias, simule 1000 realizaciones y compare los resultados.
Explique si este procedimiento garantiza exactamente seis miembros en cada
realización. No use ruleta para sustituir la regla indicada.

## Por qué practicar esta variante

PC1 P2 no pedía otra implementación de la ruleta: describía un mecanismo distinto.
Ambos mecanismos coinciden en sus esperanzas, pero no en toda su distribución.
Esta variante usa los mismos datos de la pregunta anterior precisamente para
mostrar esa diferencia. Que los promedios terminen cerca no permite intercambiar
los procedimientos cuando el profesor exige uno determinado.

## Solución matemática y por qué es correcta

La aptitud promedio es $\bar f=240/6=40$. Entonces:

$$
a=(0.25,\;0.50,\;0.75,\;1,\;1.50,\;2).
$$

Escribimos $a_i=\lfloor a_i\rfloor+r_i$, donde $r_i$ está entre cero y uno.
Si $B_i$ vale uno con probabilidad $r_i$ y cero en otro caso, el conteo generado
es $C_i=\lfloor a_i\rfloor+B_i$. Su esperanza se calcula SIN redondear:

$$
E[C_i]=\lfloor a_i\rfloor+E[B_i]
=\lfloor a_i\rfloor+r_i=a_i.
$$

Por ejemplo, para aptitud 60 resulta $a_i=1.5$: siempre se entrega una copia
y, con probabilidad 0.5, otra. El resultado de una realización es uno o dos,
jamás 1.5 cromosomas. Su PROMEDIO esperado es 1.5. Para aptitud 80, $a_i=2$:
se entregan siempre dos copias, porque su parte fraccionaria es cero.

| Aptitud | Copias seguras | Probabilidad de copia adicional | Esperanza |
| ---: | ---: | ---: | ---: |
| 10 | 0 | 0.25 | 0.25 |
| 20 | 0 | 0.50 | 0.50 |
| 30 | 0 | 0.75 | 0.75 |
| 40 | 1 | 0 | 1 |
| 60 | 1 | 0.50 | 1.50 |
| 80 | 2 | 0 | 2 |

Las esperanzas acumuladas en 1000 realizaciones son
`(250,500,750,1000,1500,2000)`. Sus valores enteros en ESTE ejemplo se deben a los
datos elegidos; no existe una regla general que obligue a la esperanza a ser entera.

## Código

```python
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
```

## Explicación del código por bloques

**`f_promedio` y `ncount`.** La expresión `f.sum()/n` calcula el promedio sin
introducir `np.mean`. Dividir cada aptitud entre ese promedio produce los valores
$a_i$ del enunciado. Estos valores no son probabilidades: algunos son mayores
que uno, por lo que no se deben usar como probabilidades de un solo evento.
Se descomponen en una parte determinista y otra probabilística.

**Parte segura.** Dentro del bucle de cromosomas, `np.floor` obtiene la parte
entera inferior, e `int` permite sumarla como cantidad de copias. Se agrega en
CADA realización. Si un cromosoma tiene dos copias seguras, tras mil realizaciones
aportará dos mil copias aunque ninguna decisión aleatoria le dé una extra.
No hay que volver a sumar esa parte al final: ya está acumulada.

**Parte aleatoria.** La comparación `np.random.rand()<fraccion` es un sorteo
Bernoulli: un uniforme cae por debajo de $r_i$ con probabilidad $r_i$. Por eso
se agrega exactamente una copia cuando se cumple la condición. Si $r_i=0$,
la condición no se cumple; si $r_i=0.75$, se cumple aproximadamente en tres
cuartas partes de muchas llamadas. No se sortea cuál de todos los cromosomas
gana esa copia: se sortea por separado para cada uno.

**Comparación final.** `copias/k` aproxima la esperanza por realización, mientras
que `copias` se compara con `k*ncount`. Se muestran también los totales para
comprobar la diferencia con la ruleta. Usar el mismo rótulo «promedio» para
`copias` sería incorrecto: ese arreglo contiene un acumulado, no un promedio.

## ¿El tamaño es siempre seis?

**No.** Hay cuatro copias seguras en total y cuatro decisiones con probabilidad
positiva de agregar una copia. Por eso una realización puede tener entre cuatro
y ocho miembros. Su esperanza sí es seis:

$$
E\!\left[\sum_i C_i\right]=\sum_iE[C_i]=6.
$$

La ruleta de la pregunta 1 llena exactamente seis plazas. Este mecanismo controla
la cantidad ESPERADA, no el tamaño exacto de cada población. Si la suma observada
en mil realizaciones no es exactamente 6000, eso no demuestra que el código esté
mal. Forzarla a 6000 o introducir otra ruleta cambiaría el procedimiento pedido.

Si modifican las aptitudes, vuelve a calcular $\bar f$, parte entera y fracción.
Lo que debes conservar es esa descomposición, no las copias numéricas de la tabla.
