# Simulacro PC1–PC2: solo enunciados

Preguntas nuevas de entrenamiento; no constituyen un anuncio del examen real.
Sin semillas ni funciones que oculten los métodos pedidos. Solo la pregunta 8 solicita gráfico.


# Pregunta 1. Selección por ruleta sin `choice`

Se tienen seis cromosomas con aptitudes `(10,20,30,40,60,80)`. La población nueva
debe tener seis miembros, seleccionados con reemplazo mediante ruleta.
Calcule las probabilidades de selección y las copias esperadas de cada cromosoma.
Simule **1000 poblaciones nuevas**, no solamente 1000 selecciones, utilizando
acumuladas y `while`. Compare esperanza y observación tanto por población como
en el total de las repeticiones. No use semilla, `choice` ni gráficos.


# Pregunta 2. Parte entera y copia adicional aleatoria

Use las aptitudes `(10,20,30,40,60,80)`. Para cada cromosoma defina
$a_i=f_i/\bar f$. En cada realización asigne la parte entera de $a_i$ como copias
seguras y una copia adicional con probabilidad igual a su parte fraccionaria.
Calcule la esperanza de copias, simule 1000 realizaciones y compare los resultados.
Explique si este procedimiento garantiza exactamente seis miembros en cada
realización. No use ruleta para sustituir la regla indicada.


# Pregunta 3. Enteros equiprobables y justificación de frecuencias

Escriba una función que genere un entero pseudoaleatorio entre dos límites
inclusivos `a` y `b`, utilizando uniformes y parte entera. Genere 1000 enteros
entre **-2 y 5**, cuente las apariciones de cada valor y compare con la cantidad
esperada. Justifique matemáticamente esa cantidad. No utilice `randint`,
semillas ni gráficos en esta pregunta.


# Pregunta 4. Primer problema de esquemas: contar posibilidades

Un espacio de búsqueda contiene **32768 puntos**, representados por todas las
cadenas de un código binario de longitud fija. La población tiene 40 individuos.
Calcule: a) longitud del cromosoma; b) total de esquemas posibles; c) total de
puntos de búsqueda; d) esquemas compatibles con un individuo; e) cotas generales
inferior y superior para los esquemas distintos representados en la población.
Escriba un programa sencillo que reporte estos resultados, sin enumerar todos
los esquemas. No se exige que los individuos sean diferentes entre sí.


# Pregunta 5. Segundo problema de esquemas: siguiente generación

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


# Pregunta 6. Codificación binaria concatenada de tres variables

Una función de tres variables utiliza $x\in[-3,5]$, $y\in[0,1000]$ y
$z\in[-0.5,0.5]$. Se requieren separaciones de malla no mayores que 0.1, 10 y
0.001, respectivamente. Determine el mínimo número de bits de cada variable y
el total. Codifique y concatene, en orden x-y-z, los puntos `(-3,0,-0.5)`,
`(5,1000,0.5)` y `(1,500,0.125)`. Decodifique las cadenas para verificar la
aproximación. Use bucles y operaciones básicas; no utilice `ceil`, `log2`,
`format` ni conversiones directas de enteros a cadenas binarias.


# Pregunta 7. Dos descendientes y conteo de mutaciones

Implemente una función de cruzamiento simple que reciba dos padres binarios y
una posición de corte, y retorne **dos descendientes complementarios**. Aplíquela
a `10110110` y `01001001`, cortando después de los primeros tres bits.
Luego implemente una función que invierta un bit con probabilidad $p_m$.
Para cada $p_m\in\{0.1,0.01,0.001\}$, haga 1000 llamadas independientes, comenzando
con bit cero EN CADA llamada, y compare el número esperado y observado de
mutaciones. No grafique ni fije semilla.


# Pregunta 8. Algoritmo genético completo con dos hijos por pareja

Maximice $F(x)=2x^4+1$ en el intervalo **[-2,3]** mediante un algoritmo genético
binario simple con selección proporcional, cruzamiento de un punto que produzca
dos hijos y mutación independiente por bit. La separación de la malla debe ser
como máximo **0.01**. Use 20 individuos, $p_c=0.8$, $p_m=0.01$ y 80 generaciones;
explique el papel de estos parámetros, sin presentarlos como óptimos universales.
Reporte el mejor individuo de la población final y haga una gráfica de la mejor
aptitud de cada generación, incluyendo la población inicial. No agregue semilla,
`choice`, elitismo ni animación. Justifique además el máximo teórico de referencia.

