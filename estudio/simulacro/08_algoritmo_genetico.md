# Pregunta 8. Algoritmo genético completo con dos hijos por pareja

## Enunciado

Maximice $F(x)=2x^4+1$ en el intervalo **[-2,3]** mediante un algoritmo genético
binario simple con selección proporcional, cruzamiento de un punto que produzca
dos hijos y mutación independiente por bit. La separación de la malla debe ser
como máximo **0.01**. Use 20 individuos, $p_c=0.8$, $p_m=0.01$ y 80 generaciones;
explique el papel de estos parámetros, sin presentarlos como óptimos universales.
Reporte el mejor individuo de la población final y haga una gráfica de la mejor
aptitud de cada generación, incluyendo la población inicial. No agregue semilla,
`choice`, elitismo ni animación. Justifique además el máximo teórico de referencia.

## Por qué practicar esta variante

PC2 P3 y el script genético justifican una pregunta que integre evaluación,
selección, cruce y mutación. Aquí el dominio está definido y la precisión tiene
un significado explícito; por tanto, no hay que inventar límites al resolver.
Se pide un gráfico, así que en ESTE ejercicio sí corresponde Matplotlib.
La función es nueva y permite comprobar analíticamente la respuesta sin exigir
que una ejecución estocástica alcance siempre el óptimo.

## Solución matemática y decisiones

**Codificación.** Como el intervalo tiene ancho cinco, deben cumplirse
$5/(2^l-1)\le0.01$. Con ocho bits el paso es $5/255\approx0.0196078$ y no sirve.
Con nueve es $5/511\approx0.00978474$, que sí sirve. Por eso el cromosoma tiene
**nueve bits**, no nueve por costumbre ni porque el script anterior tuviera otra
longitud. La decodificación es:

$$
d=\sum_{j=0}^{8}b_j2^{8-j},\qquad x=-2+5\frac{d}{511}.
$$

El código de todos ceros representa -2 y el de todos unos representa 3.
Se usan ambos extremos, algo que hay que verificar antes de confiar en los
resultados de un programa que diga trabajar en ese intervalo.

**Aptitud y selección.** Se maximiza una función que es siempre positiva:
$F(x)=2x^4+1\ge1$. Por eso se puede usar directamente como aptitud y seleccionar
con $p_i=F(x_i)/\sum_jF(x_j)$. No hace falta sumar un epsilon ni desplazar por
el mínimo. Esa modificación sería una decisión adicional innecesaria aquí.
La selección produce veinte padres con reemplazo mediante acumuladas y `while`.

**Población y tasas.** Veinte es un tamaño par, por lo que se forman diez parejas
y cada una produce dos hijos: se mantiene exactamente el tamaño. No demuestra
que veinte sea el mejor tamaño posible: es un valor fijado para practicar un
programa pequeño. $p_c=0.8$ significa cruzar una pareja con probabilidad 0.8,
no cortar el 80% de los genes. $p_m=0.01$ se aplica a CADA bit; en un hijo de
nueve bits se esperan $9(0.01)=0.09$ inversiones. Son parámetros del enunciado,
no una garantía de convergencia ni valores que debas copiar en cualquier examen.

**Máximo de referencia.** $x^4$ aumenta al aumentar $|x|$. En [-2,3] la mayor
magnitud es tres, por lo que el máximo se alcanza en $x=3$ y vale
$F(3)=2(3^4)+1=\boxed{163}$. La cadena de nueve unos lo representa exactamente.
Se calcula este valor para evaluar la búsqueda, NO para introducir ese cromosoma
artificialmente en la población ni sustituir con él el resultado encontrado.

## Código

```python
import numpy as np
import matplotlib.pyplot as plt


def F(x):
    return 2 * x**4 + 1


def translateDNA(pop):
    pesos = 2**np.arange(bits)[::-1]
    return a + (b - a) * pop.dot(pesos) / (2**bits - 1)


def select(pop, fitness):
    p = fitness / fitness.sum()
    acumulada = np.cumsum(p)
    seleccionados = pop.copy()
    for i in range(len(pop)):
        u = np.random.rand()
        j = 0
        while j < len(pop) - 1 and u >= acumulada[j]:
            j = j + 1
        seleccionados[i] = pop[j]
    return seleccionados


def crossover_(padre_1, padre_2, corte):
    hijo_1 = np.concatenate((padre_1[:corte], padre_2[corte:]))
    hijo_2 = np.concatenate((padre_2[:corte], padre_1[corte:]))
    return hijo_1, hijo_2


def mutate(hijo):
    for j in range(len(hijo)):
        if np.random.rand() < pm:
            hijo[j] = 1 - hijo[j]
    return hijo


a = -2
b = 3
precision = 0.01
bits = 1
while (b - a) / (2**bits - 1) > precision:
    bits = bits + 1

n = 20
pc = 0.8
pm = 0.01
generaciones = 80
pop = np.random.randint(2, size=(n, bits))
mejores = np.zeros(generaciones + 1)
mejores[0] = np.max(F(translateDNA(pop)))

for t in range(generaciones):
    fitness = F(translateDNA(pop))
    padres = select(pop, fitness)
    nueva = padres.copy()

    for i in range(0, n, 2):
        hijo_1 = padres[i].copy()
        hijo_2 = padres[i + 1].copy()
        if np.random.rand() < pc:
            corte = np.random.randint(1, bits)
            hijo_1, hijo_2 = crossover_(padres[i], padres[i + 1], corte)
        nueva[i] = mutate(hijo_1)
        nueva[i + 1] = mutate(hijo_2)

    pop = nueva
    mejores[t + 1] = np.max(F(translateDNA(pop)))

x = translateDNA(pop)
valores = F(x)
indice = np.argmax(valores)
print("Bits:", bits)
print("Paso de la malla:", (b - a) / (2**bits - 1))
print("Mejor cromosoma final:", pop[indice])
print("Mejor x de la poblacion final:", x[indice])
print("Valor encontrado:", valores[indice])
print("Maximo teorico de referencia:", F(b))
plt.plot(np.arange(generaciones + 1), mejores)
plt.title("Mejor aptitud por generacion; referencia teorica: 163")
plt.show()
```

## Explicación del código por bloques

**`F` y `translateDNA`: evaluar no es seleccionar.** La primera función calcula
la aptitud de los reales. La segunda convierte filas binarias a reales: las
potencias descendentes corresponden al peso de cada bit y `.dot(pesos)` obtiene
el entero de cada fila. El factor `(b-a)` y el término `a` son ambos necesarios.
Así se evita el error de multiplicar solo por el extremo superior, que puede
terminar buscando en un intervalo distinto al anunciado.

**`select`: copiar padres con probabilidad proporcional.** Primero normaliza
las aptitudes y construye la acumulada. Luego hace veinte sorteos y copia en
cada fila al individuo elegido. `seleccionados=pop.copy()` reserva una población
independiente: escribir una fila de salida no debe alterar las filas de entrada
que todavía pueden seleccionarse. Algunos padres pueden repetirse y otros no
aparecer; eso es justamente selección con reemplazo.

**`crossover_`: dos resultados de un mismo evento.** Recibe dos filas y un corte
interior ya elegido, y devuelve los hijos complementarios. Al recorrer parejas
con `range(0,n,2)`, el programa usa las filas 0–1, 2–3, y así sucesivamente.
Hace UN sorteo para decidir si cruza esa pareja y UN corte para ambos hijos.
Elegir un padre y un corte independientes para cada hijo sería otro mecanismo,
no el cruzamiento simple cuya estructura estamos practicando.

**`mutate`: un sorteo por gen.** Recorre cada posición del hijo e invierte su
bit cuando el uniforme es menor que `pm`. Se llama por separado para ambos
descendientes, por lo que cada uno tiene sus propias decisiones de mutación.
Cuando no se cruza la pareja se conservan copias de sus padres, pero esas copias
todavía pasan por mutación; «no cruzar» no significa «no aplicar ningún operador».

**Inicialización y ciclo.** `randint(2,size=(n,bits))` crea veinte filas de nueve
bits sin imponer una semilla. El ciclo evalúa la población actual, selecciona
padres, construye por completo la población siguiente y solo después hace
`pop=nueva`. Separar `padres` de `nueva` evita que un hijo ya generado se use por
accidente como padre de otra pareja dentro de la misma generación.

**Historial y gráfico.** `mejores[0]` corresponde a la población inicial.
Después de cada reemplazo se evalúa la nueva población y se guarda su mayor
aptitud en `mejores[t+1]`. Por eso hay 81 valores para las generaciones 0 a 80,
sin desplazar la gráfica una generación respecto a los datos. El gráfico muestra
mejor aptitud ACTUAL, no mejor histórico garantizado. No se usa elitismo para
forzar que la curva sea creciente; eso introduciría una característica excluida.

**Resultado final.** `np.argmax(valores)` entrega la posición del mejor miembro
de la población FINAL, no su aptitud. Con ese índice se imprimen su cadena,
su valor real y su aptitud. El máximo teórico 163 se muestra aparte, claramente
rotulado. No se anuncia como resultado encontrado si el algoritmo obtiene menos.

## Qué concluir de una ejecución

Si obtiene 163, encontró el óptimo de este ejercicio. Si termina por debajo,
encontró una aproximación o convergió a una región subóptima; no se debe falsificar
la salida ni afirmar que un algoritmo genético garantiza el máximo en 80 pasos.
La curva puede descender porque el mejor miembro puede perderse al seleccionar,
cruzar o mutar. Una curva plana tampoco prueba optimalidad sin compararla con la
referencia analítica, y volver a ejecutar puede producir resultados distintos.

El tope de 80 generaciones es el criterio de parada dado. Se evalúan la población
inicial y ochenta poblaciones siguientes; repetir ciertos cálculos de aptitud en
el código no significa haber generado generaciones adicionales. No se incorporan
paradas adaptativas, múltiples ensayos comparativos o métricas adicionales que
el enunciado no solicita.

## Cómo adaptar el ejercicio a otra función

Cambiar la función puede obligar a revisar la aptitud, no solo reemplazar `F`.
Si toma valores negativos, ya no sirve automáticamente una ruleta proporcional
a esos valores. Si cambia el intervalo o la precisión, deben recalcularse bits
y mapeo. Si piden minimización, seleccionar más a los valores grandes de la
función original sería lo contrario de lo requerido. Primero identifica qué
debe favorecer la selección y después adapta el código; no traslades una plantilla
sin verificar las premisas del problema.
