# Teoría genética para reconocer y justificar ejercicios

Referencias: Goldberg capítulos 1–3; localizadores completos en el mapa de temas.
Aquí se resumen resultados pertinentes, no todos los desarrollos algebraicos del libro.

## 1. Selección proporcional y conteo de copias

Con aptitudes `f_i >= 0`, suma positiva y población de tamaño `n`:

\[
p_i=\frac{f_i}{\sum_j f_j},\qquad
\bar f=\frac{\sum_j f_j}{n},\qquad
E[C_i]=np_i=\frac{f_i}{\bar f}.
\]

Para simular la ruleta, formar la acumulada y localizar en qué intervalo cae UN
uniforme por selección. Hacer `n` selecciones para cada nueva población, con
reemplazo. No usar `choice` si se exige el procedimiento de clase.

En el método alternativo de PC1 P2, sea `a_i=f_i/f_promedio`:

\[
C_i=\lfloor a_i\rfloor+B_i,\quad
P(B_i=1)=a_i-\lfloor a_i\rfloor,
\quad E[C_i]=a_i.
\]

Esto produce copias enteras en cada realización, pero una esperanza posiblemente
fraccionaria. El tamaño total tiene esperanza `n`; con sorteos Bernoulli
independientes NO tiene por qué ser exactamente `n` en cada realización.
No confundirlo con una selección residual que fuerza tamaño fijo.

## 2. Contar esquemas antes de aplicar el teorema

Una cadena binaria de longitud `l` pertenece a `{0,1}^l`. Un esquema usa
`{0,1,*}^l`, donde `*` admite ambos bits. Las compatibilidades se revisan solo
en posiciones fijas; un esquema representa un CONJUNTO, no un individuo extra.

| Cantidad | Resultado | Por qué |
| --- | --- | --- |
| Cadenas distintas | `2**l` | Dos opciones por posición. |
| Esquemas posibles | `3**l` | Tres símbolos por posición, incluido el esquema de todos `*`. |
| Esquemas compatibles con un individuo | `2**l` | En cada posición: su bit o `*`. |
| Cadenas compatibles con esquema de orden `r` | `2**(l-r)` | Solo las posiciones comodín son libres. |
| Esquemas de orden exactamente `r` | `binom(l,r)*2**r` | Elegir posiciones fijas y sus valores. |

Para esquemas DISTINTOS representados por una población no vacía de tamaño `n`:

\[
2^l\le S\le\min(3^l,n2^l).
\]

Son cotas generales, no necesariamente ajustadas si se exige que los `n` individuos
sean distintos. No son cotas de cantidad de cromosomas de la siguiente generación.

## 3. Orden, longitud y aptitud de un esquema

- `o(H)`: cantidad de bits fijos.
- `delta(H)`: índice de último bit fijo menos índice de primero; con cero o uno
  se toma cero. NO es la longitud total del cromosoma ni el número de comodines.
- `m(H,t)`: número de representantes presentes, contando copias de individuos.
- `f_H`: promedio de aptitud SOLO entre esos representantes, no su suma.
- `f_promedio`: promedio de toda la población actual.

Ejemplo didáctico: `H=1**0*1` tiene longitud 6, orden 3 y longitud definitoria 5.
Un esquema sin representantes no tiene promedio empírico de aptitud definido;
no dividir entre cero ni inventar ese promedio.

## 4. Teorema de esquemas

Goldberg pp. 28–33 / PDF 46–51. Bajo selección proporcional, cruce de un punto
con corte uniforme entre `l-1` lugares interiores y mutación independiente por bit:

\[
E[m_{seleccion}(H)\mid P_t]
=m(H,t)\frac{f_H}{\bar f}.
\]

Una cota conservadora de supervivencia por cruce es
`1-pc*delta(H)/(l-1)`. La probabilidad de NO alterar los bits fijos por mutación
es exactamente `(1-pm)**o(H)`; para `pm` pequeña se aproxima por `1-o(H)*pm`.
Esta es supervivencia de las posiciones fijas, no de toda la cadena.

La forma usual de primer orden del libro es:

\[
E[m(H,t+1)\mid P_t]\ge
m(H,t)\frac{f_H}{\bar f}
\left[1-p_c\frac{\delta(H)}{l-1}-o(H)p_m\right].
\]

**Interpretación:** cantidad esperada, no un entero observado ni una garantía
de conservar ese mínimo en cada ejecución. La cota ignora creación favorable de
esquemas. Si el término entre corchetes resulta negativo, esa cota es poco útil;
el conteo esperado sigue siendo no negativo. No aplicar esta expresión de cruce
de un punto sin más al cruce por máscara del script GA.

Para resolver: identificar representantes, calcular ambos promedios, contar orden,
ubicar extremos fijos, sustituir tasas y explicar la cota. Si faltan datos, dar la
expresión simbólica y señalar lo ausente. No producir un número inventando población.

Si bajo un supuesto ideal el factor de crecimiento es constantemente `1+c`, entonces
`m_t=m_0*(1+c)**t`. Es una idealización temporal; las aptitudes relativas pueden
cambiar y una población finita impone límites. No extrapolar crecimiento ilimitado.

La distinción entre cota de esperanza y conteo realizado también se contrasta en
el trabajo primario [The Exact Schema Theorem, de Alden H. Wright](https://arxiv.org/abs/1105.3538).
Es una verificación complementaria, NO una nueva lectura atribuida al profesor.

## 5. Codificación concatenada de variables reales

Goldberg pp. 82–84 / PDF 100–102. Para una variable en `[a,b]` con `l` bits:

\[
d=\sum_{j=0}^{l-1}b_j2^{l-1-j},\qquad
x=a+(b-a)\frac{d}{2^l-1},\qquad
\Delta x=\frac{b-a}{2^l-1}.
\]

Elegir el mínimo `l` tal que `Delta x<=eps`; equivale a
`l=ceil(log2((b-a)/eps+1))`. Puede buscarse con `while` y potencias de dos
para no introducir funciones de logaritmo de base 2 si se pide estilo estricto.
Codificar un real usa el entero más cercano en esa malla y luego su binario.
Concatenar en orden fijo; decodificar por separado con los límites de cada variable.
El objetivo de minimizar no cambia estas reglas de codificación.

## 6. Operadores y límites de las conclusiones

- Cruce simple: `A[:c]+B[c:]` y `B[:c]+A[c:]`. El signo `+` expresa unión de
  segmentos, NO suma elemento a elemento de arrays; el ejemplo usa `concatenate`.
- Con padres de diez bits, seis primeros bits como prefijo (`c=6`), `1011101011`
  y `0000110100` dan `1011100100` y `0000111011`. Ambos usan el mismo corte.
- Si no se cruza la pareja, conservar los dos padres como descendientes.
- Mutación por bit: invertirlo con probabilidad `pm`. En `k` llamadas a UN bit,
  el número esperado de mutaciones es `k*pm`; no confundir con el estado final.
- Bandits (pp. 36–40): explican el compromiso explorar/explotar; no son otro
  operador que haya que añadir al código solicitado.
- Procesamiento útil (pp. 40–41): no todos los esquemas contados sobreviven con
  alta probabilidad. La estimación de paralelismo implícito no es tiempo `O(n^3)`
  del programa ni una garantía de resolver cada problema eficientemente.
- Bloques constructores (pp. 41–46): hipótesis de combinar esquemas cortos,
  de bajo orden y buena aptitud. NO un teorema de convergencia al óptimo global.
- Engaño/epistasis (pp. 46–53): interacciones entre genes pueden hacer que las
  mejores decisiones parciales no conduzcan a la mejor combinación.
- Hiperplanos (pp. 53–54): cada patrón fija unas coordenadas y deja libres otras.

Estos últimos temas pertenecen al capítulo 2 indicado, pero los archivos de clase
no documentan un programa específico para cada uno. No añadirlos a una solución
de ruleta o cruce solo porque se estudian en el libro.
