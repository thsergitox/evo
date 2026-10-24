# Simulación: método, justificación y reconocimiento del código

Fuentes: Ross, segunda edición en español; TXT y PDF desarrollados del curso.
El mapa separa lo mostrado en código de lo incluido solo en la lectura 4–5.

## 1. Esperanza, conteos y Monte Carlo

Ross 2.5 y 2.7, pp. 10–17 / PDF 21–28; 3.2, pp. 38–42 / PDF 49–53.

\[
E[X]=\sum_x xP(X=x),\qquad
\widehat{E[X]}=\frac1k\sum_{s=1}^kX_s,
\qquad
\widehat{P(X=j)}=\frac{\#\{s:X_s=j\}}{k}.
\]

La ley de los grandes números justifica el promedio con muestras independientes
e idénticamente distribuidas y esperanza absoluta finita. NO afirma que una
simulación finita deba coincidir exactamente con el valor teórico.
Para indicadores, `E[I_A]=P(A)`; por linealidad, `E[C_A]=k*P(A)`.

Para `U` uniforme en `(0,1)`, `E[g(U)]=integral_0^1 g(x)dx`. En `[a,b]`,
promediar `(b-a)*g(a+(b-a)*U)`. El TXT de MC usa `exp(U)`, cuya media es `e-1`.
El promedio acumulado al paso `s` divide entre `s`, desde **1**, no desde 0.

## 2. Inversa discreta y uniforme entera

Ross 4.1, pp. 45–50 / PDF 56–61.

Para probabilidades `p_j`, formar `F_j=p_1+...+p_j`; elegir el primer intervalo
de la acumulada que contiene el uniforme. El TXT de TI implementa la búsqueda
con `while`. Se necesita suma de probabilidades 1 y valores no negativos.
En código finito, cuidar los extremos y no seleccionar una categoría de masa cero
si el generador produce exactamente un extremo; la partición puede usarse como
`F_anterior <= U < F_actual`.

Para enteros inclusivos `[a,b]`, hay `m=b-a+1` valores:

\[
X=a+\lfloor mU\rfloor,\quad P(X=j)=1/m,
\quad E[C_j]=k/m.
\]

En PC1: `m=10`, `k=1000`, así que `E[C_j]=100`. La fórmula y el conteo de valores
son la justificación que debe acompañar el resultado, no solo «todos son iguales».

## 3. Binomial negativa por recurrencia

Ross ejercicio 4.10(b,c), p. 59 / PDF 70. Aquí se cuentan ENSAYOS hasta `r` éxitos:

\[
p_j=\binom{j-1}{r-1}p^r(1-p)^{j-r},\quad j\ge r,
\qquad p_{j+1}=\frac{j(1-p)}{j+1-r}p_j.
\]

El PDF inicia `j=r`, `p_=p**r`, `F=p_`; un uniforme fija la meta. El `while`
agrega masas sucesivas hasta alcanzarla. `x[i]=j` guarda el número de ensayos.
La recurrencia evita calcular factoriales en cada paso. Con `r=3,p=.3`, la media
es `r/p=10`. No sustituir esta implementación por un generador de fallos antes
de `r` éxitos: tendría otro soporte y no mostraría el método pedido.

## 4. Aceptación-rechazo y condicionamiento

Ross 4.4, pp. 53–56 / PDF 64–67; ejercicio 4.13, p. 59 / PDF 70.

Con distribución objetivo `p_j`, propuesta `q_j` y `c>=sup(p_j/q_j)`, generar
`Y~q`, `U` uniforme independiente y aceptar con probabilidad `p_Y/(c*q_Y)`.
La probabilidad total de aceptar es `1/c`; el número medio de propuestas es `c`.
La propuesta debe cubrir todo punto de masa objetivo positiva.

El TXT AR usa propuesta uniforme en diez valores: `Q=.1`, `c=1.2`. El `while`
regenera propuesta y uniforme hasta aceptar. Luego cuenta y estima probabilidades.

Para `Y` con ley de `X~Binomial(n,p)` condicionada a `X>=k`,

\[
P(Y=j)=\frac{P(X=j)}{\alpha},\quad j\ge k,
\qquad \alpha=P(X\ge k)>0.
\]

Se genera una binomial y se rechaza cuando no cumple `X>=k`. Aceptar una propuesta
cuesta en promedio `1/alpha` intentos: si `alpha` es pequeña, el rechazo es lento.
El PDF usa un uniforme adicional contra un indicador 0/1; la idea es aceptación
determinista por el evento. No confundir esto con la inversa de la ley condicionada.

## 5. Producto de uniformes y conteo Poisson

Ross ejercicio 3.13, p. 44 / PDF 55. Se define
`N=max{n:producto(U_1,...,U_n)>=exp(-3)}`, con producto vacío igual a 1.
Al tomar menos logaritmos, `-log(U_i)` son exponenciales de razón 1, y la
desigualdad cuenta llegadas acumuladas hasta tiempo 3. Así `N~Poisson(3)`:

\[
E[N]=3,\qquad P(N=j)=e^{-3}\frac{3^j}{j!}.
\]

En el código, `u` contiene el producto; el `while` continúa mientras se cumple
el umbral; `N[i]` cuenta productos admitidos antes de cruzarlo. No sumar otra
unidad por el producto que ya incumple. Las frecuencias para `0,...,6` NO tienen
por qué sumar 1: la distribución también admite `N>6`.

## 6. Inversa continua y composición

Ross 5.1, pp. 62–66 / PDF 73–77; ejercicios 5.7 y 5.8(b), p. 82 / PDF 93.
Si `F` es continua e invertible y `U` uniforme, `F**(-1)(U)` tiene distribución `F`.
Para exponencial de razón `lambda`, puede usarse `-log(U)/lambda` con `U>0`.

Si `F=sum(w_i*F_i)`, elegir primero componente `I` con probabilidades `w_i`,
y después generar de `F_I`. La mezcla desarrollada es:

\[
F(x)=\tfrac13 F_{Exp(2)}(x)+\tfrac23 F_{U(0,1)}(x).
\]

Con probabilidad `1/3`, generar `-log(U)/2`; en otro caso, otro uniforme. Para
`x<=0`, `F(x)=0`; para `0<x<1`, `F(x)=(1-exp(-2*x)+2*x)/3`; para `x>=1`,
`F(x)=(3-exp(-2*x))/3`. Su media es `(1/3)*(1/2)+(2/3)*(1/2)=1/2`.
El uniforme que decide componente y el que genera su valor deben ser sorteos
independientes, como en el ejemplo. No sumar los dos valores: es mezcla, no suma.

## 7. Resto de capítulos 4–5: lectura, sin script adjunto para cada método

- **Poisson 4.2:** `p_0=exp(-lambda)`, `p_(j+1)=lambda*p_j/(j+1)` y acumulada.
- **Binomial 4.3:** `p_0=(1-p)**n`, recurrencia
  `p_(j+1)=p_j*(n-j)*p/((j+1)*(1-p))`, para `0<p<1`; o contar éxitos Bernoulli.
  Los casos `p=0,1` son deterministas y no usan esa división.
- **Composición discreta 4.5:** seleccionar una distribución componente y generar
  de ella; misma idea estructural que la mezcla continua.
- **Rechazo continuo 5.2:** sustituir masas por densidades, con `f(x)<=c*g(x)`;
  la probabilidad de aceptación sigue siendo `1/c`.
- **Polar 5.3:** generar `V1,V2` uniformes en `(-1,1)`, rechazar si
  `S=V1**2+V2**2` no está en `(0,1)`, y producir
  `Z_i=V_i*sqrt(-2*log(S)/S)`. Son DOS normales estándar independientes.
- **Poisson homogéneo 5.4:** sumar tiempos exponenciales de razón `lambda` hasta
  superar `T`; los tiempos admitidos son las llegadas y el conteo es Poisson `lambda*T`.
- **Poisson no homogéneo 5.5:** adelgazamiento con tasa superior `M>=lambda(t)`:
  proponer tiempos de un Poisson homogéneo de razón `M` y aceptar el evento en `t`
  con probabilidad `lambda(t)/M`. El capítulo también trata generación directa.

Estas fórmulas son guía matemática, NO permiso para nuevas funciones de biblioteca.
Que un método tenga fórmula no obliga a implementarlo si la pregunta pide otro.
