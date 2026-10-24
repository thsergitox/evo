# Pregunta 3. Enteros equiprobables y justificación de frecuencias

## Enunciado

Escriba una función que genere un entero pseudoaleatorio entre dos límites
inclusivos `a` y `b`, utilizando uniformes y parte entera. Genere 1000 enteros
entre **-2 y 5**, cuente las apariciones de cada valor y compare con la cantidad
esperada. Justifique matemáticamente esa cantidad. No utilice `randint`,
semillas ni gráficos en esta pregunta.

## Por qué practicar esta variante

PC1 P3 y la práctica dirigida contienen el mismo tipo de pregunta. El feedback
pedía justificar el 100, no solo imprimirlo. Al cambiar a un intervalo que tiene
ocho valores, la respuesta ya no puede ser 100: hay que identificar el número
de resultados posibles y multiplicar su probabilidad por las repeticiones.
El extremo negativo también permite comprobar que el desplazamiento está bien.

## Solución matemática y por qué es correcta

Los valores posibles son `-2,-1,0,1,2,3,4,5`. Hay $m=b-a+1=8$ resultados, no
siete: se cuentan ambos extremos. Para un uniforme $U$ en $[0,1)$,
la variable $\lfloor8U\rfloor$ toma los valores de cero a siete. Cada uno se
obtiene en un intervalo de ancho $1/8$, de modo que todos son equiprobables.
Al sumar $a=-2$, se desplaza ese conjunto al intervalo solicitado:

$$
X=a+\lfloor(b-a+1)U\rfloor=-2+\lfloor8U\rfloor.
$$

Para cualquier entero $j$ entre -2 y 5 se cumple $P(X=j)=1/8$. Sea $C_j$ su
conteo en los mil sorteos. Como $C_j=\sum_{s=1}^{1000}I(X_s=j)$, y la esperanza
de un indicador es la probabilidad de su evento, se obtiene:

$$
E[C_j]=\sum_{s=1}^{1000}P(X_s=j)=1000\frac18=125.
$$

Por eso se esperan 125 apariciones DE CADA valor. No es una división arbitraria:
es la suma de las probabilidades de aparición a lo largo de las repeticiones.
Esta es la explicación que debes poder reconstruir si cambian cualquiera de los
dos límites o la cantidad de sorteos.

## Código

```python
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
```

## Explicación del código por bloques

**La función `entero_aleatorio`.** Recibe los límites que exige el enunciado.
Multiplica el uniforme por el número de enteros posibles; `floor` transforma
los ocho intervalos en índices enteros, y sumar `a` hace el desplazamiento.
El `int` cambia el tipo numérico de la salida, no la probabilidad de los valores.
No se debe hacer `floor(8*U-2)` por una regla memorizada sin entenderla, aunque
en este caso el desplazamiento entero haga que coincida: la fórmula general
con `a` separado deja claros soporte y cantidad de categorías.

**El primer `for`.** Cada iteración llama de nuevo a la función y guarda UNA
observación en `x`. Como hay mil iteraciones, hay mil enteros generados. Aquí no
existe un bucle interior que forme una población: no se debe multiplicar otra
vez por ocho el tamaño de la muestra. Ocho es la cantidad de resultados posibles,
no el número de sorteos que se hacen en cada repetición.

**El segundo `for`.** El índice `j` recorre de cero a siete, pero los valores
reales son `a+j`, es decir, de -2 a 5. `x.tolist().count(a+j)` cuenta cuántas
observaciones coinciden con ese valor. Omitir `a` haría contar cero a siete,
lo que perdería los negativos y agregaría categorías que no pertenecen al soporte.
El método de conteo es el mismo que aparece en el TXT de inversa discreta.

**La comparación impresa.** El valor teórico `k/m` se repite para todas las
categorías porque son equiprobables. Los conteos observados son enteros y su
suma es exactamente mil. El programa muestra ambos sin modificar lo observado
para que parezca más cercano al teórico: esa diferencia es parte del experimento.

## Qué concluir y cómo adaptar el ejercicio

Obtener 118 apariciones de -2 y 132 de 5 no refuta la uniformidad ni invalida la
esperanza 125. Esta última es una media de repeticiones hipotéticas del experimento,
no una condición que deba cumplirse exactamente en cada muestra de mil valores.
La explicación correcta es que las frecuencias fluctúan alrededor de su referencia.

Si vuelven a pedir 1000 números entre 3 y 12, hay diez resultados y se obtiene
$1000/10=100$. Si piden 2000 entre esos mismos límites, se esperan 200 de cada
uno. El procedimiento mental es siempre **contar el soporte, hallar su probabilidad
y multiplicar por el número de sorteos**, no memorizar 100.
