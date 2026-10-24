# Pregunta 4. Primer problema de esquemas: contar posibilidades

## Enunciado

Un espacio de búsqueda contiene **32768 puntos**, representados por todas las
cadenas de un código binario de longitud fija. La población tiene 40 individuos.
Calcule: a) longitud del cromosoma; b) total de esquemas posibles; c) total de
puntos de búsqueda; d) esquemas compatibles con un individuo; e) cotas generales
inferior y superior para los esquemas distintos representados en la población.
Escriba un programa sencillo que reporte estos resultados, sin enumerar todos
los esquemas. No se exige que los individuos sean diferentes entre sí.

## Por qué practicar esta variante

Es el mismo patrón de PC2 P1 a–d con números nuevos. No requiere simular un
algoritmo genético: se está midiendo la estructura de su representación. Introducir
selección, mutación o generaciones sería trabajo adicional que la pregunta no pide.
También comprueba que no se confundan tres cantidades parecidas: cadenas posibles,
esquemas posibles y esquemas compatibles con una cadena concreta.

## Solución matemática y por qué es correcta

Si cada posición admite dos bits y hay $l$ posiciones, existen $2^l$ cadenas.
Como $32768=2^{15}$, el cromosoma tiene **15 bits**. La igualdad es exacta por
la condición del enunciado: se representan todos los puntos por todas las cadenas.
Si el número de puntos no fuera potencia de dos, habría que distinguir capacidad
del código y puntos efectivamente válidos; no sería la misma premisa.

Un esquema admite `0`, `1` o `*` en cada posición. Por el principio multiplicativo,
hay $3^l$ patrones: cada una de las $l$ elecciones tiene tres alternativas.
Se incluye el esquema que tiene solo asteriscos, pues representa todo el espacio.
Por tanto, el total de esquemas posibles es $3^{15}=14348907$, NO $2^{15}$.

Para contar esquemas compatibles con UN individuo, cada posición admite solo
dos opciones: mantener SU bit o reemplazarlo por `*`. No puede elegirse el bit
contrario, porque dejaría de ser compatible. Por eso esta cantidad es $2^{15}=32768$.
Por ejemplo, la cadena `10` pertenece a `10`, `1*`, `*0` y `**`: cuatro esquemas,
aunque el universo completo de esquemas de longitud dos tiene nueve.

Para una población no vacía, al menos están representados los esquemas de uno
de sus individuos. En el extremo de todos los individuos iguales se alcanza ese
mínimo. Una cota superior se obtiene sumando $2^l$ por cada individuo, aunque
esa suma cuente repeticiones; además, nunca se puede superar el universo $3^l$:

$$
2^l\le S\le\min(3^l,n2^l).
$$

Con $n=40$ y $l=15$ resulta:

$$
32768\le S\le\min(14348907,40\cdot32768)=1310720.
$$

Estas son cotas generales, no una cantidad exacta de esquemas presentes ni una
afirmación de que la cota superior siempre se alcance. Dos individuos pueden
compartir muchos esquemas: se cuentan patrones DISTINTOS, no su multiplicidad.

## Código

```python
puntos = 32768
n = 40
l = 0

while 2**l < puntos:
    l = l + 1

total_esquemas = 3**l
por_individuo = 2**l
inferior = por_individuo
superior = n * por_individuo
if superior > total_esquemas:
    superior = total_esquemas

print("Longitud binaria:", l)
print("Puntos de busqueda:", 2**l)
print("Esquemas posibles:", total_esquemas)
print("Esquemas compatibles con un individuo:", por_individuo)
print("Cota inferior general:", inferior)
print("Cota superior general:", superior)
```

## Explicación del código por bloques

**El `while` de la longitud.** Empieza con $2^0$ y aumenta `l` mientras esa
cantidad sea menor que el número de puntos. Al terminar, encuentra 15 porque
$2^{14}<32768$ y $2^{15}=32768$. Se usa una búsqueda con potencias de dos,
sin introducir funciones de logaritmo o redondeo. Es un conteo determinista:
no necesita números aleatorios ni semilla.

**Las potencias resuelven preguntas distintas.** `3**l` representa todos los
patrones con comodines; `2**l` representa cadenas y, por un argumento distinto,
también el número de esquemas compatibles con un individuo. Que dos resultados
numéricos coincidan no significa que el concepto sea igual. En una respuesta de
examen conviene escribir la explicación de las opciones por posición, no limitarse
a presentar tres potencias sin decir qué cuenta cada una.

**La condición de la cota superior.** El programa primero calcula `n*2**l` y
solo la reduce a `3**l` si supera el universo. Esa comparación es la operación
mínimo escrita con un `if`, de modo que no se necesita otra función de biblioteca.
En estos datos no se reduce porque $1310720<14348907$. No se está generando
la población: basta conocer su tamaño para establecer esta cota general.

## Error típico y adaptación

No uses $3^l$ como cantidad de puntos de búsqueda: el asterisco es un símbolo
de una plantilla, no un tercer valor del gen binario. Tampoco se deduce de esta
pregunta cuántos individuos habrá de un esquema en la siguiente generación:
para eso hacen falta las aptitudes y operadores del problema siguiente.
Si cambian el tamaño del espacio, recalcula `l`; si cambian la población, cambia
la cota superior, pero no el universo de esquemas de esa longitud.
