# Preparación del parcial

Revisión del 23 de octubre de 2026. Se consultaron los siete PDF, cuatro scripts
TXT y los dos notebooks disponibles. No se modificaron las entregas ni los libros.
Esta documentación general es una auditoría y una guía de estudio. El nuevo
[simulacro ampliado resuelto](simulacro/README.md) está separado de las entregas.

## Por dónde comenzar

1. `AGENTS.md`, en la raíz: reglas para cualquier ayuda futura.
2. [Mapa de temas y libros](MAPA_TEMAS_Y_LIBROS.md): qué estudiar y dónde.
3. [Funciones de clase](INVENTARIO_FUNCIONES.md): evidencia y restricciones.
4. [Auditoría PC1](AUDITORIA_PC1.md): feedback, unidades y código adicional defectuoso.
5. [Auditoría PC2](AUDITORIA_PC2.md): correspondencia por bloques y dos descendientes.
6. [Teoría genética](TEORIA_GENETICA.md) y [simulación](TEORIA_SIMULACION.md).
7. `fuentes/`: copias Python de lectura para ubicar líneas sin abrir Colab.
8. [Simulacro de PC1 y PC2](simulacro/README.md): ocho preguntas nuevas, con
   enunciados sin respuestas, notebook resuelto y explicaciones por bloques.

## Qué es cada material

| Material original | Papel en el estudio |
| --- | --- |
| `pc1/1erLabCalificado_CS521_.pdf` | Enunciado de ruleta, conteo de copias y uniforme entera. |
| `pc1/Sergio_pezo_1er_Lab_Calificado_CS521.ipynb` | Tu solución actual; incluye una segunda versión de P2 que debe aislarse. |
| `pc2/2daCalificada_CS521_.pdf` | Enunciado de esquemas, codificación y optimización genética. |
| `pc2/PezoSergio_PC2.ipynb` | Tu solución actual: P2 obtuvo 8/8; P3 no debe usarse como plantilla sin revisión. |
| `pc2/2doLabDirigido_CS521_.pdf` | Ejercicios y código de selección y cruzamiento con dos hijos. |
| `ProblemasDesarrollados_.pdf` | Cuatro ejercicios de Ross: Monte Carlo, inversa, rechazo y composición. |
| `Segunda Práctica Dirigida CM-274 - ProblemasDesarrollados_.pdf` | Misma secuencia de problemas y código; la extracción de sus símbolos es peor. No son ocho ejercicios independientes. |
| `Semana 02_Monte Carlo_.txt` | Estimadores acumulados: moneda e integral de exp(x). |
| `metTI__discreto.txt` | Transformada inversa discreta y uniforme entera. |
| `metA-R_discreto.txt` | Aceptación-rechazo discreto. |
| `script_GA basico.txt` | Algoritmo genético de referencia: tiene animación, `choice` y cruce por máscara. No es una autorización universal. |
| Ross | Simulación, segunda edición en español; capítulos 4–5 indicados por el usuario, más los antecedentes/ejercicios localizados. |
| Goldberg | Genetic Algorithms in Search, Optimization, and Machine Learning (1989); capítulo 2 indicado por el usuario; también se localizaron ejercicios exactos en capítulos 1 y 3. |

## Feedback conservado

**PC1: 9/20, según el usuario**

- P1: 3/8. «\"Se utilizó una semilla 12 para reproductibilidad\"??...no se pide esta condicion»;
  no usar `np.random.choice`, sino lo visto en clase; «numero esperado no es una fraccion».
- P2: 4/8. «Incorrecto. Numero esperado no es una fraccion».
- P3: 2/4. «Falta justificar porque numero esperado es 100».

**PC2: 15/20 al sumar los puntajes comunicados**

- P1: 6/8. «a) incorrecto».
- P2: 8/8.
- P3: 1/4. «Tiene que generar 2 cromosomas».

Son transcripciones del mensaje, no anotaciones verificadas en una rúbrica adjunta.
No sabemos si los notebooks actuales son idénticos a las versiones calificadas.

## Acuerdos y límites

- Mínimo código necesario, con `for`/`while` y métodos visibles de clase.
- Sin semillas ni visualizaciones adicionales. Un gráfico requerido sí se entrega.
- No es correcto convertir «la esperanza no es fracción» en una ley matemática.
  Hay una discrepancia que debe aclararse sin alterar las fórmulas correctas.
- El libro sí contiene el teorema de esquemas en el capítulo 2. El número exacto
  de preguntas del parcial NO puede verificarse con los archivos disponibles.
- No se encontró otro solucionario del profesor para la PC2 calificada. Sí hay
  una práctica dirigida y el script genético. No atribuirles una solución inexistente.

## Copias y extracción

- `fuentes/*`: cuatro TXT convertidos sin cambios de código a Python; ambos
  notebooks transcritos con celdas numeradas desde 1; dos transcripciones de los
  bloques de código impresos en PDF. NO se han corregido ni ejecutado.
- `.context/extracted/`, en la raíz: texto por PDF. En Ross, los saltos de página
  conservan el localizador físico. Goldberg no tenía texto: el archivo
  `Goldberg_secciones_OCR.txt` contiene solo las secciones consultadas, con marcas
  `PDF n`. OCR significa reconocimiento óptico de caracteres: puede errar fórmulas.
- Se renderizaron PNG temporales para revisar fórmulas y páginas; se retiraron
  después de la revisión. Los PDF originales siguen siendo la referencia ante
  errores de extracción.

## Ruta sugerida

1. Justificar los 100 de PC1 P3 y separar las cinco cantidades de PC1 P1.
2. Reconstruir selección con acumuladas usando el TXT de inversa.
3. Entender y dibujar un cruzamiento que conserve ambos hijos.
4. Repetir la codificación de PC2 P2, que ya obtuvo puntaje completo.
5. Estudiar esquemas: compatibilidad, orden, longitud, supervivencia y cota.
6. Repasar inversa, rechazo y composición de Ross con sus cuatro ejercicios.

Para una revisión posterior se puede pedir: «Revisa este archivo con `AGENTS.md`:
indica qué bloque resuelve cada inciso, qué funciones no tienen evidencia de clase
y cuál es el cambio mínimo. No añadas funcionalidades».
