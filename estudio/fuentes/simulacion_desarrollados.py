# TRANSCRIPCIÓN DE LECTURA; NO CORREGIDA NI AUTÓNOMA.
# Fuente: /home/sergi/Documents/semesters/nine/dl/evo/ProblemasDesarrollados_.pdf
# Se omiten enunciados y fórmulas. Algunos fragmentos requieren np/plt previos.

# %% Monte Carlo: media y probabilidades
k=1000
N=np.zeros(k)
for i in np.arange(k):
  u=np.random.rand()
  while u>=np.exp(-3):
    u=u*np.random.rand()
    N[i]=N[i]+1
k_=np.arange(1,k+1)
N_=np.cumsum(N)/k_
print(N_[k-1]) # imprime utlimo valor estimado
plt.plot(k_,N_)
plt.show()
pesos_=np.zeros(7)
for j in np.arange(len(pesos_)):
  pesos_[j]=N.tolist().count(j)

plt.bar(np.arange(7),pesos_/len(N),width = 0.4)
print(pesos_/len(N))

# %% Binomial negativa: inversa
import pandas as pd
n=500;r=3;pr=0.3
x=np.zeros(n)
for i in np.arange(n):
  j=r;p_=pr**r;F=p_;u=np.random.rand()
  while u >= F:
    p_=((j*(1-pr))/(j+1-r))*p_
    F=F+p_
    j=j+1
  x[i]=j

x_values=np.asarray(np.unique(x), dtype="int")
pesos_=np.zeros(len(x_values))
for j in np.arange(len(x_values)):
  pesos_[j]=x.tolist().count(x_values[j])

plt.bar(x_values,pesos_/len(x),width = 0.8)
plt.title("Binomial Negativa - Transformada Inversa")
print(pesos_/len(x))

# %% Binomial condicionada: rechazo
n=10;p=0.3;k=4
x=np.zeros(1000)
for i in range(len(x)):
 y=np.random.binomial(n,p,1)
 u=np.random.rand()
 while u > np.float64(y>=k):
  y=np.random.binomial(n,p,1)
  u=np.random.rand()
 x[i]=y

xx=np.zeros(n-k+1)
for j in np.arange(len(xx)):
 xx[j]=x.tolist().count(j+k)

plt.bar(np.arange(n-k+1)+k,xx/len(x),width = 0.4)
print(xx/len(x))

# %% Mezcla exponencial y uniforme
k=1000
x=np.zeros(k)
for i in np.arange(k):
 if np.random.rand()<(1/3):
   x[i]=-(1/2)*np.log(np.random.rand())
 else:
   x[i]=np.random.rand()

plt.hist(x,bins=None,cumulative=True, range=None,density=True)
plt.show()
