# Reglas del curso: Computación Evolutiva

## Objetivo y alcance

Preparar y revisar ejercicios con el método del profesor: código sencillo,
operaciones visibles y justificación matemática. Este archivo se llama
`AGENTS.md` (no `AGN.md`). La documentación de apoyo está en `estudio/README.md`.
Las reglas generales de `/home/sergi/AGENTS.md` siguen aplicándose.

## Fuentes y prioridades

1. Enunciado del ejercicio actual y aclaraciones expresas del profesor.
2. Feedback de las PC, conservando su alcance y señalando contradicciones.
3. Código entregado en TXT y en las prácticas dirigidas.
4. Libros para justificar la matemática, NO para autorizar nuevas funciones.
5. Notebooks del alumno como material que se AUDITA, no como estilo autorizado.

No atribuir al profesor una regla deducida solo del código del alumno. Ante una
contradicción, mostrar ambas evidencias; no corregir la teoría para adivinar una
rúbrica. No afirmar que vendrán exactamente dos problemas de esquemas: es una
comunicación oral reportada por el alumno, sin anuncio escrito en estos archivos.

## Código mínimo

- Resolver únicamente lo solicitado. Preferir `for`, `while`, `if`, contadores,
  acumuladores, índices y arreglos básicos. No agregar clases ni infraestructura.
- Consultar `estudio/INVENTARIO_FUNCIONES.md` antes de introducir una función.
  Estar instalada una biblioteca NO significa tener permiso para usarla.
- Para selección discreta/ruleta, usar las acumuladas y la búsqueda con `while`
  de clase; NO `np.random.choice` por defecto. El feedback de PC1 lo rechaza,
  aunque aparezca en el script genético de referencia.
- No fijar semillas: PC1 rechazó `np.random.seed(12)` por no estar solicitado.
  Tampoco reutilizar la semilla 7 de PC2 en nuevas soluciones sin indicación.
- No agregar gráficos, animaciones, histogramas ni tablas si no se solicitan.
  Si se pide gráfica, SÍ hacerla: PC2 pregunta 3 pide convergencia.
- No agregar Pandas por el solo hecho de que hay un import sin uso en un PDF.
- No sustituir el método pedido por generadores directos de distribuciones:
  si se pide inversa, implementar la inversa; si se pide rechazo, mostrar rechazo.
- No agregar elitismo, escalamiento, tasas, límites ni precisión arbitrarios.
  Un parámetro elegible debe justificarse; un dato indispensable ausente se indica.
- Funciones pequeñas cuando el enunciado las pida o el ejemplo pertinente las use.
  No convertir cada operación en una función ni ocultar el algoritmo en atajos.
- Comentarios explican la decisión o el concepto; no narran cada asignación.
- Preservar originales. Las copias en `estudio/fuentes/` son de lectura, NO
  soluciones corregidas ni scripts garantizados como autónomos.
- No ejecutar builds. Para documentación/transcripción basta revisión de fuentes,
  sintaxis y cálculos puntuales; no crear entornos o suites por defecto.

## Contratos que no se pueden cambiar

- Ruleta: `p_i = f_i / sum(f)`, con aptitudes no negativas y suma positiva.
  Cada nueva población tiene `n` selecciones CON reemplazo.
- Conteo de copias: `a_i = f_i / f_promedio`; dar `floor(a_i)` copias y UNA
  adicional con probabilidad `a_i - floor(a_i)`. No convertirlo en otra ruleta.
- Uniforme entera inclusiva: `a + floor((b-a+1)*U)`.
- Cruzamiento simple de dos padres: un MISMO corte produce DOS hijos
  complementarios; no confundirlo con poner `n=2` en la población.
- Mutación: sortear cada bit con probabilidad `pm`; cambiar `0` por `1` o viceversa.
- Codificación real: `x = a + (b-a)*d/(2**l-1)`. Verificar ambos extremos.
- Si se exige precisión `eps`, elegir el mínimo `l` tal que
  `(b-a)/(2**l-1) <= eps`, y justificarlo, no solo imprimir los bits.

## Teoría y unidades obligatorias

- Diferenciar probabilidad `p_i`, esperanza por población `n*p_i`, esperanza
  acumulada en `k` poblaciones `k*n*p_i`, conteo observado y promedio observado.
  Una esperanza PUEDE ser fraccionaria; un conteo observado es entero. No redondear
  expectativas para obedecer literalmente una observación ambigua.
- Para 1000 sorteos uniformes entre 3 y 12: hay `12-3+1=10` valores;
  `P(X=j)=1/10`, luego `E[C_j]=1000/10=100`. Escribir esta justificación.
- En binomial negativa, la práctica cuenta ENSAYOS hasta `r` éxitos:
  soporte `r,r+1,...`, no fallos con soporte `0,1,...`.
- Un esquema binario usa `{0,1,*}`. Para longitud `l`: `2**l` cadenas,
  `3**l` esquemas posibles, `2**l` esquemas compatibles con un individuo.
  En una población no vacía de tamaño `n`, cotas generales para esquemas distintos:
  `2**l <= S <= min(3**l, n*2**l)`; no sumar duplicados como esquemas diferentes.
- Orden `o(H)`: posiciones fijas. Longitud definitoria `delta(H)`: última posición
  fija menos primera; con cero o una posición fija se toma cero.
- Teorema de esquemas, forma usual de primer orden para cruce de UN punto:
  `E[m(H,t+1) | población_t] >= m(H,t)*(f_H/f_promedio)*`
  `(1-pc*delta(H)/(l-1)-o(H)*pm)`, con `l>1` y supuestos de selección proporcional.
  Es una cota de esperanza, NO un conteo garantizado ni prueba de óptimo global.
  Definir cada término; no inventar valores ausentes para obtener un decimal.

Detalles: `estudio/TEORIA_GENETICA.md` y `estudio/TEORIA_SIMULACION.md`.
Páginas y alcance real: `estudio/MAPA_TEMAS_Y_LIBROS.md`.

## Protocolo para explicar o revisar una solución

1. Identificar enunciado, pregunta/inciso y salida pedida.
2. Dar la idea matemática y las unidades del resultado.
3. Señalar la fuente de clase equivalente, con página/bloque o líneas.
4. Relacionar cada bloque del código con la parte que resuelve.
5. Separar errores matemáticos, incumplimientos de estilo y datos faltantes.
6. Proponer el cambio mínimo; no reescribir una respuesta correcta por estética.
7. Comprobar tamaño, soporte, probabilidades, extremos y número de descendientes.
8. No preguntar y seguir trabajando: si una pregunta requiere respuesta, detenerse.

Cuando se soliciten simulacros o soluciones para estudiar, incluir enunciado,
desarrollo matemático, código y explicación por bloques en párrafos completos.
Explicar POR QUÉ funciona el procedimiento, qué significa la salida y cómo se
adapta a datos nuevos; no sustituirlo por comentarios de una línea. Las posibles
preguntas futuras son inferencias basadas en las PC, nunca predicciones seguras.

## Checklist de entrega

- [ ] Cada inciso tiene respuesta y justificación breve.
- [ ] No hay semillas, importaciones, funciones ni salidas no solicitadas.
- [ ] Cada función empleada tiene evidencia y cumple el método exigido.
- [ ] Esperanzas, frecuencias, promedios y conteos están rotulados sin confusión.
- [ ] El cruce devuelve dos descendientes cuando corresponde.
- [ ] Dominio, precisión y parámetros están dados o justificados explícitamente.
- [ ] Si piden convergencia, se muestra su gráfico; si no, no se agrega.
- [ ] No se copiaron errores de los ejemplos de clase ni salidas antiguas sin revisar.
