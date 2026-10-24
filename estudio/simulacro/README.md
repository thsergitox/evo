# Simulacro ampliado: variantes de PC1 y PC2

Preparado el 23 de octubre de 2026. **Son preguntas nuevas de entrenamiento,
no preguntas filtradas ni una predicción confirmada del parcial.** Los datos,
intervalos y parámetros se eligieron para este simulacro y están indicados en
cada enunciado: no se presentan como datos proporcionados por el profesor.

## Abrir y estudiar

- **`Simulacro_PC1_PC2_Resuelto.ipynb`**: las ocho preguntas, desarrollo matemático,
  código ejecutable, explicaciones por bloques y resultados de una ejecución.
- **`ENUNCIADOS.md`**: las ocho preguntas sin respuestas, para intentar resolverlas.
- **`01_*.md` a `08_*.md`**: soluciones individuales con explicación y código.
- **`01_*.py` a `08_*.py`**: código de cada ejercicio, independiente de los demás.

No necesitas memorizar una salida aleatoria. Lee el enunciado, intenta resolverlo,
y después compara la fórmula, el procedimiento y las unidades con la solución.
Las preguntas 4 y 5 son las DOS variantes de esquemas que conviene dominar;
esto no demuestra que el examen real vaya a tener exactamente dos.

## Por qué seleccioné estas variantes

| Pregunta | Tema | Evidencia de las prácticas | Qué cambio respecto al material anterior |
| --- | --- | --- | --- |
| 1 | Ruleta con acumuladas | PC1 P1; feedback rechaza `choice`. | Aptitudes nuevas; se distingue una población de mil poblaciones. |
| 2 | Parte entera y copia adicional | PC1 P2. | Misma población nueva para comparar métodos sin confundirlos. |
| 3 | Uniforme entera y esperanza de frecuencias | PC1 P3 y dirigida P2. | Intervalo con negativos y esperanza 125, no 100 memorizado. |
| 4 | Conteo de esquemas | PC2 P1 a–d. | Nuevo tamaño del espacio y de la población. |
| 5 | Teorema de esquemas | PC2 P1 e y Goldberg capítulo 2. | Población, esquema, aptitudes y tasas explícitas; nada se inventa al resolver. |
| 6 | Codificación de tres variables | PC2 P2, calificada con 8/8. | Nuevos límites y precisiones; cálculo con bucles, sin `ceil/log2/format`. |
| 7 | Dos hijos y mutación | Dirigida P3–P4; feedback de PC2 P3. | Padres nuevos, un mismo corte y prueba de un bit independiente. |
| 8 | Algoritmo genético completo | PC2 P3 y script GA. | Dominio definido, función nueva, dos hijos por pareja y gráfica pedida. |

Es una inferencia por similitud temática. No se asignan porcentajes de probabilidad
porque no existe evidencia que permita estimarlos. Para repaso focalizado: 1, 4, 5,
6 y 7 primero; la 8 integra los operadores. La 2 y la 3 completan lo evaluado en PC1.
Los métodos adicionales de Ross siguen en la guía general; no se les atribuye aquí
una presencia segura en un examen basado en las PC.

## Reglas aplicadas

Sin semillas, `np.random.choice`, Pandas, elitismo ni animaciones. Las funciones
de biblioteca proceden del inventario de clase. Se usa `.sum()` del script GA,
no `np.mean`, `np.sum`, `np.ceil`, `np.log2` ni funciones de codificación nuevas.
El único gráfico está en la pregunta 8 porque su enunciado lo solicita.
Los bucles conservan visible el procedimiento; los comentarios largos y la
justificación se dejan en las celdas de texto, no como ruido dentro del código.

Las preguntas estocásticas muestran una ejecución de ejemplo. Sus resultados
cambiarán al ejecutar de nuevo. El teórico se compara con lo observado, no se
fuerza la muestra a coincidir exactamente ni se redondean las esperanzas por regla.

## Fuentes locales para contrastar

El [mapa del curso](../MAPA_TEMAS_Y_LIBROS.md) contiene las páginas de Goldberg
y Ross. El [inventario](../INVENTARIO_FUNCIONES.md) documenta las llamadas de clase.
Las [auditorías de PC1](../AUDITORIA_PC1.md) y [PC2](../AUDITORIA_PC2.md) separan
errores, feedback confirmado y contradicciones pendientes.

No se modificaron los notebooks calificados ni los scripts originales.
Se reutilizó el entorno Python existente en el directorio padre para verificar
las ocho soluciones y generar el gráfico; no se creó un entorno ni se instalaron
paquetes. No se ejecutaron builds.
