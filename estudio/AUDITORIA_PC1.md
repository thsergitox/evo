# PC1: qué resolvía el código y qué revisar

Fuentes: enunciado de PC1, notebook actual y feedback transcrito en `README.md`.
Referencias de código: `fuentes/pc1_entrega_original.py`. Las celdas se cuentan
desde 1 incluyendo Markdown; los originales se preservaron sin ejecutar.

## Pregunta 1: ruleta — 3/8

| Parte | Código actual | Qué resuelve |
| --- | --- | --- |
| Datos y probabilidad | Celda 4; `f`, `n`, `k`, `p=f/np.sum(f)` | Las seis aptitudes, seis selecciones por población y mil repeticiones. |
| Valor teórico | `n_esp=n*p` | Esperanza de copias de cada cadena en UNA población. |
| Muestreo | `np.random.choice(...)` dentro del `for` | Hace la ruleta estadísticamente, pero oculta el método que el profesor exigía. |
| Conteo | `x.tolist().count(j)` | Cuenta copias; el arreglo `copias` ACUMULA mil poblaciones. |
| Estimación | `copias/k` | Promedio observado por población, no conteo total. |

**Incumplimientos expresos:** semilla 12 no solicitada y uso de `choice` rechazado.
La adaptación mínima futura es la inversa discreta de `metTI__discreto.txt`:
acumulada, uniforme por selección, índice y `while`. No añadir gráficos.

**Discrepancia matemática:** el enunciado pide número esperado de copias y
Goldberg problema 1.6, p. 24 / PDF 42, usa exactamente las mismas aptitudes.
Aquí `sum(f)=205`, de modo que `E[C_i]=6*f_i/205`. No es un error que no sea entero.
El comentario «no es una fracción» no identifica por sí solo la escala requerida.
Además, Goldberg distingue explícitamente conteo esperado decimal y conteo real
entero en la tabla 2.1, p. 34 / PDF 52; en p. 33 / PDF 51 calcula una esperanza
de 3.20 copias y la compara con tres copias realizadas. No son la misma cantidad.

| Aptitud | Probabilidad | Esperanza por población | Esperanza en 1000 poblaciones |
| ---: | ---: | ---: | ---: |
| 5 | 5/205 | 0.146341 | 146.341463 |
| 10 | 10/205 | 0.292683 | 292.682927 |
| 15 | 15/205 | 0.439024 | 439.024390 |
| 25 | 25/205 | 0.731707 | 731.707317 |
| 50 | 50/205 | 1.463415 | 1463.414634 |
| 100 | 100/205 | 2.926829 | 2926.829268 |

Las esperanzas suman 6 y 6000 respectivamente. Los conteos OBSERVADOS sí son
enteros; que se impriman como `146.` por el dtype no cambia su naturaleza.
Para evitar confusión, separar cinco rótulos: probabilidad, esperanza por población,
esperanza acumulada, conteo observado y promedio observado. NO redondear el valor
teórico para convertirlo artificialmente en entero. El criterio exacto del docente
sobre esta observación queda pendiente, no se presenta una hipótesis como certeza.

## Pregunta 2: control del número esperado — 4/8

**Celda 6, líneas 100–133:**

1. `f_=np.mean(f)` obtiene la aptitud media.
2. `ncount=f/f_` obtiene las mismas esperanzas por cadena que en P1.
3. `ent=np.floor(ncount[j])` da copias seguras.
4. `frac=ncount[j]-ent`, y el `if` contra un uniforme, añaden una copia Bernoulli.
5. `copias` acumula los resultados de mil realizaciones.

Este mecanismo coincide con la definición del enunciado y Goldberg 1.7. No hay
evidencia para concluir que el mecanismo sea incorrecto solo porque la esperanza
es decimal. El comentario antes de imprimir dice «promedio», pero se imprime
`copias`, que es TOTAL. Además, el Markdown relata promedios mientras el código
imprime esperanzas y observaciones acumuladas: hay que unificar la presentación.

El tamaño generado por este procedimiento puede variar; la esperanza total es 6.
Forzarlo a seis en cada repetición cambiaría el algoritmo especificado.

### No usar como plantilla la celda 7 adicional

El mismo notebook contiene OTRA implementación en las líneas 136–163. No se
conoce su procedencia; no se atribuye al profesor. Tiene problemas independientes:

- `np.modf` y otras llamadas no quedan autorizadas por aparecer en TU notebook.
- `while` está fuera del bucle de `i`; se pierden los sorteos de las columnas
  anteriores. Solo queda el último `i` y muchas posiciones de `xx` permanecen cero.
- `xx[j,i]` está DENTRO del `while`: si no entra, no se guarda siquiera la categoría.
- `P` guarda partes fraccionarias, pero `P_` usa `a_i/6`, no esas partes. Volver a
  sortear una ruleta completa y añadir las partes enteras no es el mecanismo pedido.
- `P_*k*6+k*P_entera` añade de nuevo copias ya incluidas en la esperanza completa.
  Su suma es 9000, frente a las 6000 copias esperadas por el procedimiento de P2.

No basta «arreglar la indentación»: también está equivocado el algoritmo que esta
variante intenta implementar. Conservarla como evidencia de revisión, no ejecutarla
como segunda respuesta ni mezclar sus resultados con la primera implementación.

## Pregunta 3: uniforme entera — 2/4

**Celda 9, líneas 185–227:** `entero_aleatorio(a,b)` implementa
`a+floor((b-a+1)*U)`; el primer `for` genera las 1000 observaciones y el segundo
cuenta cada resultado. La idea corresponde al TXT TI y a Goldberg tarea C, p. 25.

El Markdown actual ya dice que hay diez valores equiprobables, pero falta desarrollar
explícitamente el paso de probabilidad a esperanza que pide justificar el feedback:

\[
12-3+1=10,\quad P(X=j)=\tfrac1{10},\quad
C_j=\sum_{s=1}^{1000}I(X_s=j),\quad E[C_j]=1000\tfrac1{10}=100.
\]

El 100 es una ESPERANZA, no una exigencia de obtener exactamente cien veces cada
entero. Retirar la semilla en nuevas entregas. Mantener la función porque el
enunciado sí la pide; no reemplazarla por un generador directo que oculte la fórmula.

## Orden de corrección recomendado

1. Retirar en la futura versión las semillas y cambiar la ruleta a acumuladas.
2. Rotular y comparar magnitudes en la misma escala, manteniendo la esperanza real.
3. Usar una sola implementación de P2; la primera refleja el mecanismo solicitado.
4. Añadir la justificación de P3 por indicadores o linealidad.
5. Aclarar con el profesor el criterio sobre «fracción» antes de cambiar resultados
   que son consistentes con el enunciado y el libro.

No se reescribieron las respuestas durante esta auditoría ni se atribuyó una causa
exacta a cada punto perdido más allá del feedback que se proporcionó.
