# Inventario de funciones y operaciones observadas

**Observada no significa autorizada en cualquier pregunta.** Este inventario cubre
los archivos disponibles, no todas las clases que pudo haber dictado el profesor.
Las referencias L son líneas de los TXT originales; los PDF se localizan por página.

## Claves de fuentes

- **MC**: `Semana 02_Monte Carlo_.txt`.
- **TI**: `metTI__discreto.txt`.
- **AR**: `metA-R_discreto.txt`.
- **GA**: `script_GA basico.txt`.
- **SD1/SD2**: `ProblemasDesarrollados_.pdf`, página 1/2.
- **DG**: `pc2/2doLabDirigido_CS521_.pdf`, única página.
- **PC2-P2**: celda 7 del notebook del alumno; obtuvo 8/8 según el feedback.

## NumPy: datos, cuentas y generación

| Función/operación | Evidencia | Uso y límite |
| --- | --- | --- |
| `np.array` | TI L4; AR L3; DG P1 | Especificar datos/probabilidades. |
| `np.zeros` | TI L6,L14; AR L6,L15; SD1,SD2; DG | Guardar muestras y contadores. |
| `np.ones` | AR L4 | Propuesta uniforme `Q`. |
| `np.arange` | TI L7,L15,L18; AR L7,L16,L19; GA L19,L23; SD; DG | Índices, soportes y potencias binarias. |
| `np.cumsum` | MC L11,L22; TI L5; SD1; DG P1 | Acumuladas o sumas acumuladas, según la variable. |
| `np.floor` | TI L25; AR L8,L11 | Uniforme entera, parte entera. |
| `np.max` | AR L5 | Constante de rechazo `c=max(P/Q)`. |
| `np.min` | GA L15 | Desplazar aptitud en el ejemplo genético. |
| `np.argmax` | GA L58,L59 | Índice del mejor individuo, no su valor. |
| `np.exp` | MC L20,L24; SD1 | Integral y umbral del producto de uniformes. |
| `np.log` | SD2 P4 | Exponencial por inversa. |
| `np.sin`, `np.pi` | GA L11 | Función objetivo particular; `pi` es una constante, no función. |
| `np.asarray`, `np.unique` | SD1 P2 | Soporte observado de binomial negativa; no autorizan ocultar el generador. |
| `np.float64` | SD2 rechazo | Conversión en condición de aceptación del ejemplo. |
| `np.random.rand` | TI L8,L25; AR L8–12; GA L29,L38; SD; DG | Uniformes para selección, rechazo y decisiones. |
| `np.random.randint` | GA L30,L31,L43; DG P3 | Inicializar bits y elegir índices/cortes; respetar qué rango exige cada tarea. |
| `np.random.binomial` | SD2 rechazo | Propuesta binomial en ESE ejercicio. No sustituir inversa por ella si se pide inversa. |
| `np.random.choice` | GA L23 | CONFLICTO: PC1 lo rechaza explícitamente. Evitar por defecto; usar acumuladas. |
| `np.linspace` | GA L46 | Malla para graficar; solo si el gráfico corresponde. |
| `np.concatenate` | DG P3 | Ensamblar los DOS hijos del cruce. |

## Métodos, Python y funciones propias

| Elemento | Evidencia | Finalidad |
| --- | --- | --- |
| `.tolist().count(valor)` | TI L16; AR L17; SD | Conteo por categoría. Son dos métodos, no una función de NumPy. |
| `.astype(int)` | AR L8,L11 | Conversión del arreglo de índices. |
| `.astype(np.bool_)` | GA L31 | Máscara de cruce uniforme; `np.bool_` es un tipo. |
| `.dot(...)` | GA L19 | Valor entero binario mediante potencias de dos. |
| `.sum()` | GA L24 | Normalizar aptitudes en ese script. |
| `.copy()` | GA L61; DG P3 | Conservar población/padre sin sobrescribirlo. |
| `len` | TI L15,L18,L19; AR L16,L19,L20; SD; DG | Tamaños de arreglos y soportes. |
| `range` | MC L9,L10,L20,L21; GA L37,L49; SD2 | Repeticiones/índices. |
| `int`, `list` | MC L9,L13,L24 | Indicador y lista de referencia. |
| `float` | GA L19 | Conversión del denominador. |
| `print` | Todos los TXT | Mostrar resultados que responden al enunciado. |
| `rd.random` | MC L9,L20 | Uniformes de `random as rd`; no introducir otro generador sin necesidad. |
| `repeat` de `itertools` | MC L4,L13,L24 | Línea de referencia; prescindible si no hay gráfico. |
| `globals`, `sca.remove()` | GA L53 | Estado de animación; no forman parte del algoritmo genético. |
| `F`, `get_fitness`, `translateDNA` | GA L11,L15,L19 | Objetivo, aptitud, decodificación. |
| `select`, `crossover`, `mutate` | GA L22,L28,L36 | Operadores del script; `crossover` devuelve UN hijo y usa máscara. |
| `crossover_` | DG P3 | Cruce de UN punto: devuelve corte y DOS hijos. Es el contrato pertinente al feedback. |

Operaciones observadas: índices/slices (`[:]`, `[::-1]`), asignación por máscara,
bucles, condicionales, comparaciones, potencias y comprensión de listas en MC.
No hace falta imitar la vectorización del GA cuando un bucle explícito es más claro.

## Visualización: permitida SOLO cuando corresponde

- `plt.plot`, `plt.show`: MC L14–16,L25–27; GA; SD1.
- `plt.bar`: TI L18; AR L19; SD1,SD2.
- `plt.title`: SD1 binomial negativa.
- `plt.hist`: SD2 mezcla.
- `plt.ion`, `plt.ioff`, `plt.scatter`, `plt.pause`: GA L45,L54,L67.
  Son animación, NO requisitos generales. Para convergencia no es obligatorio animar.
- `import pandas as pd` aparece en SD1 sin llamadas a `pd` ni tablas: no trasladarlo.

## Lo que aparece SOLO en entregas del alumno

- `np.random.seed`: PC1 y PC2; prohibir por defecto debido al feedback de PC1.
- `np.mean`, `np.sum`, `np.modf`: aparecen en PC1; no se hallaron con esos nombres
  exactos en los códigos del profesor disponibles. `.sum()` sí aparece en GA.
- `np.ceil`, `np.log2`, `round`, `format`, `str`, `sum`, `.append`, `.join`:
  usados en PC2-P2, calificada con 8/8. Esto respalda esa solución concreta,
  NO demuestra que se enseñaran todos en clase ni autoriza su uso indiscriminado.
  Si se exige lista estricta de funciones de clase, calcular bits con `while`
  es una alternativa sin `ceil/log2`; no reescribir la PC2 aprobada sin necesidad.
- Elitismo mediante `pop[0]=mejor`: añadido en PC2; no está en el GA de referencia.

## Antes de aprobar una función nueva

Buscar una llamada real en una fuente pertinente. Si no existe, marcar «sin
evidencia» y preferir operaciones conocidas. No declarar algo «prohibido por el
profesor» solo porque no apareció: la ausencia de evidencia no es una prohibición
expresa. Para nuevas soluciones, la política conservadora solicitada es no añadirlo.

## Errores y ambigüedades en el material de referencia

Imitar el método NO significa copiar errores:

- **MC L10–11:** `range(n)` empieza en cero. La primera media divide entre cero
  y las siguientes usan un denominador desplazado. La media acumulada usa `1,...,n`,
  como ya hace el segundo ejemplo de ese mismo TXT en L21–22.
- **DG P1:** las probabilidades del enunciado suman `.99`; el código cambia la
  sexta de `.10` a `.11`, con lo que suman 1. No normalizar ni corregir silenciosamente
  datos de otro ejercicio: señalar la inconsistencia y usar una aclaración explícita.
- **DG P1:** el código `zeros((20,10))` con dos bucles genera 20 grupos de diez
  selecciones, 200 selecciones, no una sola lista de veinte. Aclarar qué unidad
  representa `k` antes de reutilizarlo.
- **DG P3:** `randint(DNA_SIZE-1)` genera `0,...,8` si la longitud es diez.
  Con el slicing impreso, un cruce interior normal requiere cortes `1,...,9`.
  El cero intercambia cadenas completas y el último corte interior queda excluido.
- **GA L19:** el mapeo declarado para `[-1,2]` produce `[0,2]`; se explica en la
  auditoría PC2. No repetirlo para nuevos dominios.
- **AR/SD:** algunos bloques asumen que `np` o `plt` ya fueron importados. Las
  transcripciones de lectura no prometen ejecución autónoma ni compatibilidad de
  todos los detalles con cualquier versión de las bibliotecas.

La [documentación oficial de NumPy sobre `choice`](https://numpy.org/doc/stable/reference/random/generated/numpy.random.choice.html)
confirma su muestreo ponderado con reemplazo. Eso explica qué hace la llamada,
pero NO le da permiso académico frente a la restricción del profesor.
