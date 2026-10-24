# PC2: correspondencia entre consigna, código y estilo de clase

Fuentes: enunciado de PC2, práctica dirigida, script GA, Goldberg y notebook actual.
Los localizadores siguientes usan `fuentes/pc2_entrega_original.py`; las celdas
incluyen Markdown y empiezan en 1. Los originales permanecen sin cambios.

## Pregunta 1 — 6/8, «a) incorrecto»

| Líneas / celda 5 | Parte resuelta | Verificación |
| --- | --- | --- |
| 21–24 | Calcular longitud desde los puntos | `2**21=2097152`: 21 bits. |
| 31–32 | a: total de esquemas | `3**21=10460353203`. |
| 34–35 | b: puntos de búsqueda | `2**21=2097152`. |
| 37–38 | c: esquemas por individuo | `2**21=2097152`. |
| 40–41 | d: cotas generales | Inferior `2097152`; superior `50*2**21=104857600`. |
| 43–67 | e: cota de siguiente generación | Aplica una fórmula del teorema, pero con datos inventados. |

**Discrepancia del inciso a:** la fórmula actual coincide con Goldberg p. 29 /
PDF 47, y con la discusión de codificaciones p. 82 / PDF 100. El problema 3.2 del
libro, p. 87 / PDF 105, es el origen de a–d, pero compara binario Y octal. La PC
pide binario. No hay base para cambiar `3**l` por otra fórmula solo por el comentario
del feedback. Hace falta ver el criterio o la versión realmente evaluada.

En d se cuentan esquemas DISTINTOS, no copias. La cota superior puede escribirse
`min(3**l,n*2**l)`; aquí da el mismo resultado. Son cotas generales, no una
enumeración exacta de los esquemas presentes en una población que no se ha dado.

**Problema adicional de e, observado en el código:** `m=10`, `fH=12`,
`f_otros=9.5`, `pc=.25`, `pm=.01` y `H=11...` no están en el enunciado. Producen
`f_prom=10` y `11.61`, pero solo para ESE ejemplo añadido. No son un resultado
numérico derivable de los datos originales. La respuesta respaldada es la cota
simbólica con los términos definidos; si el profesor dio datos oralmente, faltan
en estos archivos. El feedback no los menciona, pero eso no valida inventarlos.

## Pregunta 2 — 8/8: conservar la idea

Origen exacto: Goldberg problema 3.3, pp. 87–88 / PDF 105–106; fundamento de
codificación en pp. 82–84 / PDF 100–102. **Celda 7:**

| Líneas | Qué resuelven |
| --- | --- |
| 74–75 | Intervalos y precisiones de las tres variables. |
| 78–82 | Calculan la cantidad mínima de bits por variable. |
| 84–85 | Reportan `[9,7,11]`, en total 27 bits. |
| 87 | Los tres puntos pedidos. |
| 90–99 | Recorren cada coordenada y la mapean al entero de la malla más cercano. |
| 101–102 | Representación binaria con ceros a la izquierda y ancho fijo. |
| 104–105 | Decodificación para comprobar el mapeo. |
| 107–110 | Resultados por componente y cadena concatenada. |

Prueba de minimalidad: con un bit menos la separación supera la precisión pedida.

| Variable | Bits | Separación con esos bits | Con un bit menos | Precisión requerida |
| --- | ---: | ---: | ---: | ---: |
| x | 9 | 145/511 = 0.283757 | 145/255 = 0.568627 | 0.5 |
| y | 7 | 1200000/127 = 9448.818898 | 1200000/63 = 19047.619048 | 10000 |
| z | 11 | 1.1/2047 = 0.000537372 | 1.1/1023 = 0.001075269 | 0.001 |

Los extremos producen todos ceros y todos unos. El tercer punto da:
`011110111 | 0001011 | 10100010001`. Concatenar sin separadores, en orden x-y-z.
La reconstrucción es aproximada: `[50.0880626,103937.0078740,0.5969711773]`.

No reemplazar una solución calificada con puntaje completo por una abstracción
nueva. `ceil/log2/format/round/join` quedan documentadas como usadas en esta
respuesta aceptada, no como funciones del profesor verificadas en los scripts.

## Pregunta 3 — 1/4, «Tiene que generar 2 cromosomas»

**Celda 9:**

| Líneas | Qué hace | Observación para futuras soluciones |
| --- | --- | --- |
| 119 | Fija semilla 7 | No solicitada; ya había rechazo de semillas en PC1. |
| 122–129 | Dominio y parámetros | `[-5,8]` no figura en el PDF; faltan justificaciones de n, precisión y tasas. |
| 131–136 | Función objetivo y aptitud | Objetivo correcto; el epsilon es una decisión extra no justificada. |
| 138–140 | Binario a real | Fórmula afín correcta PARA el dominio elegido. |
| 143–146 | Selección | `choice`: aparece en el script, pero entra en conflicto con el feedback de PC1. |
| 149–154 | Cruce de un punto | Devuelve UN padre modificado; pareja/corte pueden cambiar por llamada. |
| 157–161 | Mutación | Sorteo independiente por bit e inversión con `1-bit`. |
| 164 | Población inicial | Tener dos filas no demuestra producir dos hijos complementarios de cada cruce. |
| 166–184 | Ciclo de generaciones | Evalúa, selecciona y llama al cruce una vez por individuo. |
| 171–172,186–187 | Guarda/restaura mejor individuo | Elitismo añadido; no está en el script de referencia. Sobrescribe un descendiente. |
| 174–176,189–194 | Progreso y máximo final | Texto no reemplaza la gráfica de convergencia exigida. |

### Qué significa el contrato de DOS descendientes

La dirigida P3 pide una función con dos padres y un corte, y devuelve dos hijos.
En `fuentes/pc2_dirigida_profesor.py`, bloque `crossover_`, se conservan los
segmentos de ambos padres y se ensamblan de forma complementaria. Tu `crossover`
no cumple ese contrato: hace una sustitución y devuelve un solo cromosoma.
Llamarla dos veces con elecciones independientes NO es el mismo operador.

**No corregirlo simplemente con `n=2`: ya tenías `n=2`.** El tamaño poblacional
y la cantidad de resultados que devuelve un cruce son conceptos diferentes.
La relación exacta con la deducción de puntos se basa en el comentario reportado;
la dirigida es la evidencia de cómo implementar el contrato esperado.

### Datos faltantes y requisitos no satisfechos

- **Dominio:** `3*x**10` no tiene máximo finito sobre todos los reales. Para
  optimizar en un intervalo hace falta definirlo/justificarlo. Si se elige
  `[-5,8]`, el máximo es `3*8**10=3221225472`, pero es resultado de un supuesto
  añadido, no un máximo universal. No reutilizar automáticamente ese intervalo.
- **Precisión:** con ese intervalo y 12 bits, el paso es `13/4095≈0.00317460`.
  El notebook no explica por qué esa precisión es la elegida.
- **Parámetros:** no basta copiar `pc=.25`, `pm=.01`, 150 generaciones o n=2.
  El PDF pide justificación. El significado de `p_s` no se define en el PDF:
  no confundir sin aclaración probabilidad de selección con supervivencia de esquemas.
- **Gráfico:** la consigna sí lo pide; el notebook no incluye uno. Guardar por
  generación la medida de convergencia que se vaya a graficar y rotularla.
  Esto se señala como requisito independiente, no como causa confirmada del puntaje.

### El script del profesor tampoco se copia sin revisar

En `script_GA basico.txt`:

- `translateDNA`, L19, multiplica solo por `X_BOUND[1]`. Con límites `[-1,2]`
  produce `[0,2]`, no `[-1,2]`. Falta el desplazamiento y ancho correctos.
- `crossover`, L28–33, usa máscara aleatoria y produce UN hijo. Es un operador
  diferente de `crossover_` de la dirigida; no intercambiarlos por tener nombre parecido.
- `choice` está presente, pero no anula la restricción expresa de PC1.
- La animación es presentación del ejemplo, no una obligación del algoritmo.

## Siguiente revisión útil

Tomar la pregunta 3 y revisar por separado: dominio/precisión, selección,
cruce de dos hijos, mutación y convergencia. Usar la dirigida como referencia del
cruce y mantener la codificación correcta de P2. Todavía NO se creó una versión
corregida ni un nuevo notebook de entrega.
