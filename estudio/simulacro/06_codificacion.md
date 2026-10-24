# Pregunta 6. Codificación binaria concatenada de tres variables

## Enunciado

Una función de tres variables utiliza $x\in[-3,5]$, $y\in[0,1000]$ y
$z\in[-0.5,0.5]$. Se requieren separaciones de malla no mayores que 0.1, 10 y
0.001, respectivamente. Determine el mínimo número de bits de cada variable y
el total. Codifique y concatene, en orden x-y-z, los puntos `(-3,0,-0.5)`,
`(5,1000,0.5)` y `(1,500,0.125)`. Decodifique las cadenas para verificar la
aproximación. Use bucles y operaciones básicas; no utilice `ceil`, `log2`,
`format` ni conversiones directas de enteros a cadenas binarias.

## Por qué practicar esta variante

PC2 P2 fue la respuesta que obtuvo puntaje completo. Conviene conservar su
razonamiento: cada variable necesita su propia longitud y su propio mapeo.
Esta variante modifica los datos y hace visible la conversión con bucles, de
modo que puedas explicar los bits y no depender de una llamada que los oculte.
El criterio de precisión se fija aquí como separación entre puntos consecutivos,
para evitar confundirlo con otra convención de error máximo de redondeo.

## Solución matemática y por qué es correcta

Con $l$ bits hay $2^l$ enteros, de cero a $2^l-1$. Para mapearlos incluyendo
ambos extremos de $[a,b]$, existen $2^l-1$ separaciones. Por eso:

$$
x(d)=a+(b-a)\frac{d}{2^l-1},\qquad
\Delta x=\frac{b-a}{2^l-1}\le\varepsilon.
$$

No se divide entre $2^l$: hacerlo impediría que el código de todos unos llegara
exactamente al extremo superior. La longitud mínima se encuentra aumentando
$l$ hasta satisfacer la desigualdad. Para demostrar minimalidad, se verifica
además que con un bit menos no se satisface.

| Variable | Bits | Paso con esos bits | Paso con un bit menos | Límite pedido |
| --- | ---: | ---: | ---: | ---: |
| x | 7 | 8/127 = 0.0629921 | 8/63 = 0.1269841 | 0.1 |
| y | 7 | 1000/127 = 7.8740157 | 1000/63 = 15.8730159 | 10 |
| z | 10 | 1/1023 = 0.000977517 | 1/511 = 0.001956947 | 0.001 |

El total es **$7+7+10=24$ bits**. El extremo inferior de cada variable se
representa por todos ceros y el superior por todos unos. Por tanto, las dos
primeras cadenas concatenadas tienen 24 ceros y 24 unos, respectivamente.

Para convertir un real al entero de la malla más cercano se usa:

$$
d=\left\lfloor\frac{x-a}{b-a}(2^l-1)+\frac12\right\rfloor.
$$

El cociente anterior es no negativo porque los puntos pertenecen a sus intervalos.
Sumar $1/2$ y tomar parte entera elige el vecino más cercano; cuando hay empate,
esta convención elige el mayor. Para el tercer punto se obtiene:

| Variable | Entero antes de redondear | Entero seleccionado | Binario |
| --- | ---: | ---: | --- |
| x=1 | 63.5 | 64 | `1000000` |
| y=500 | 63.5 | 64 | `1000000` |
| z=0.125 | 639.375 | 639 | `1001111111` |

La cadena concatenada es **`1000000 | 1000000 | 1001111111`**, sin guardar las
barras como genes. Al decodificar se recupera aproximadamente:

$$
(1.03149606,\;503.93700787,\;0.124633431).
$$

No se recuperan exactamente los reales originales porque generalmente no
pertenecen a la malla. Eso no invalida la representación: sus errores son
aproximadamente 0.03149606, 3.93700787 y 0.000366569, menores que las precisiones
pedidas. Se preservan los límites y se conoce de antemano la separación de la malla.

## Código

```python
import numpy as np

limites = np.array([[-3, 5], [0, 1000], [-0.5, 0.5]])
precision = np.array([0.1, 10, 0.001])
puntos = np.array([[-3, 0, -0.5], [5, 1000, 0.5], [1, 500, 0.125]])
longitudes = np.zeros(3).astype(int)

for i in range(3):
    a = limites[i, 0]
    b = limites[i, 1]
    l = 1
    while (b - a) / (2**l - 1) > precision[i]:
        l = l + 1
    longitudes[i] = l

total_bits = int(longitudes.sum())
cromosomas = np.zeros((len(puntos), total_bits)).astype(int)
decodificados = np.zeros((len(puntos), 3))
print("Bits por variable:", longitudes)
print("Total de bits:", total_bits)

for t in range(len(puntos)):
    inicio = 0
    for i in range(3):
        a = limites[i, 0]
        b = limites[i, 1]
        l = longitudes[i]
        d = int(np.floor((puntos[t, i] - a) * (2**l - 1) / (b - a) + 0.5))
        resto = d

        for j in range(l - 1, -1, -1):
            cromosomas[t, inicio + j] = resto % 2
            resto = resto // 2

        d_leido = 0
        for j in range(l):
            d_leido = 2 * d_leido + cromosomas[t, inicio + j]
        decodificados[t, i] = a + (b - a) * d_leido / (2**l - 1)
        inicio = inicio + l

    print("Punto:", puntos[t])
    print("Cromosoma concatenado:", cromosomas[t])
    print("Punto decodificado:", decodificados[t])
```

## Explicación del código por bloques

**Encontrar longitudes.** El primer `for` trabaja una variable a la vez. Dentro,
el `while` comienza con un bit: empezar en cero produciría un denominador cero
en $2^l-1$. Aumenta la longitud hasta que la separación cumple el requisito y la
guarda en `longitudes`. Se conserva la responsabilidad de cada dato: los límites
de y no se usan para calcular los bits de z.

**Reservar y ubicar segmentos.** `total_bits` suma las tres longitudes. Cada fila
de `cromosomas` es una cadena completa de 24 bits. Para cada punto, `inicio`
empieza en cero y después de cada variable avanza su longitud. Esto coloca x en
las posiciones 0–6, y en las 7–13 y z en las 14–23. Concatenar significa poner
segmentos uno a continuación del otro, no sumar sus bits ni usar una longitud
única para las tres variables.

**Obtener el binario con divisiones.** El resto de dividir un entero entre dos
es su bit menos significativo. Por eso `resto%2` se coloca primero a la derecha,
y `resto//2` elimina ese bit antes de continuar hacia la izquierda. El bucle
termina después de exactamente `l` posiciones, de manera que también deja los
ceros iniciales requeridos. No se necesita una función de conversión binaria.

**Verificar leyendo los bits.** Para reconstruir el entero se recorre el segmento
de izquierda a derecha con `d_leido=2*d_leido+bit`. Por ejemplo, leer `101`
produce sucesivamente 1, 2 y 5. Ese entero se transforma otra vez a real usando
los límites correspondientes. Se leen los bits realmente generados, en vez de
imprimir simplemente el valor de entrada como si fuera una comprobación.

## Cómo adaptar el ejercicio

Si cambian intervalos o precisiones, vuelve a calcular longitudes y posiciones
de inicio. No reutilices 24 bits como una constante del método. Si solo cambia
el punto a codificar, se conserva la malla y se repite la conversión.
El hecho de que la función objetivo vaya a minimizarse o maximizarse no cambia
esta representación: eso afectará después la evaluación/selección, no el mapeo.
